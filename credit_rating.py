import logging
import argparse
import json
import pandas as pd
from pydantic import ValidationError
from models import MortgageInput

# Log config
logging.basicConfig(level=logging.ERROR,format="%(asctime)s - %(levelname)s - %(message)s")


def calculate_credit_rating(json_input: MortgageInput) -> str:
    """ This function accepts a list of mortgages and calculates the overall credit rating for the RMBS. """
    
    try:
        # Check if input list is valid
        if not isinstance(json_input, MortgageInput) or not json_input.mortgages:
            logging.error("Invalid JSON input: Missing 'Mortgages' key or incorrect format")
            return "Invalid Input"

        # Convert mortgage data to a DataFrame
        df = pd.DataFrame([m.model_dump() for m in json_input.mortgages])

        # Calculate risk factors
        df["ltv_risk"] = (df["loan_amount"] / df["property_value"]).apply(lambda x: 2 if x > 0.9 else 1 if x > 0.8 else 0)
        
        df["dti_risk"] = (df["debt_amount"] / df["annual_income"]).apply(lambda x: 2 if x > 0.5 else 1 if x > 0.4 else 0)
        
        df["credit_risk"] = df["credit_score"].apply(lambda x: -1 if x >= 700 else 1 if x < 650 else 0)
        
        df["loan_type_risk"] = df["loan_type"].apply(lambda x: -1 if x == "fixed" else 1)
        
        df["property_type_risk"] = df["property_type"].apply(lambda x: 1 if x == "condo" else 0)

        # Compute total risk score per mortgage
        df["total_risk_score"] = df[["ltv_risk", "dti_risk", "credit_risk", "loan_type_risk", "property_type_risk"]].sum(axis=1)

        # Adjust risk score based on average credit score
        avg_credit_score = df["credit_score"].mean()
        total_risk_score = df["total_risk_score"].sum()

        if avg_credit_score >= 700:
            total_risk_score -= 1
        elif avg_credit_score < 650:
            total_risk_score += 1

        # Determine credit rating
        if total_risk_score <= 2:
            return "AAA"
        elif 3 <= total_risk_score <= 5:
            return "BBB"
        else:
            return "C"

    except ValidationError as e:
        for e in e.errors():
            logging.error(f"ValidationError- Field:{e['loc'][0]} , Message:{e['msg']}")
        return "Invalid Input"
    except Exception as e:
        logging.exception(f"An exception has occured: {e}")
        return "Invalid Input"
        

if __name__ == "__main__":
    
    # Creating parser and taking input from CLI
    parser = argparse.ArgumentParser(description="Calculate RMBS credit rating")
    parser.add_argument("input_file",type=str,help="Path to the input JSON file")
    
    args = parser.parse_args()
    
    
    try:
        # Open and read the input JSON file
        with open(args.input_file, 'r') as file:
            data = json.load(file)
        
        
        # Check if input list is valid
        mortgage_input = MortgageInput(**data)
        
        rating = calculate_credit_rating(mortgage_input)
        
        print(f"Credit rating for given RMBS is: {rating}")
    
    except FileNotFoundError:
        logging.error("The input file was not found. Please provide a valid file path.")
        
    except Exception as e:
        logging.error(f"An exception has occured.{e}")