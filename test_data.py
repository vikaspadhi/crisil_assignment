VALID_MORTGAGES = {
    "mortgages": [
        {
            "credit_score": 750,
            "loan_amount": 200000,
            "property_value": 300000,
            "annual_income": 90000,
            "debt_amount": 15000,
            "loan_type": "fixed",
            "property_type": "single_family"
        },
        {
            "credit_score": 680,
            "loan_amount": 180000,
            "property_value": 250000,
            "annual_income": 70000,
            "debt_amount": 20000,
            "loan_type": "adjustable",
            "property_type": "condo"
        }
    ]
}

EDGE_CASES = {
    "mortgages": [
        {  # Minimum valid credit score (300)
            "credit_score": 300,
            "loan_amount": 100000,
            "property_value": 150000,
            "annual_income": 50000,
            "debt_amount": 5000,
            "loan_type": "fixed",
            "property_type": "single_family"
        },
        {  # Maximum valid credit score (850)
            "credit_score": 850,
            "loan_amount": 250000,
            "property_value": 500000,
            "annual_income": 150000,
            "debt_amount": 15000,
            "loan_type": "fixed",
            "property_type": "single_family"
        },
        {  # LTV exactly at 90% (high risk threshold)
            "credit_score": 700,
            "loan_amount": 180000,
            "property_value": 200000,
            "annual_income": 80000,
            "debt_amount": 15000,
            "loan_type": "adjustable",
            "property_type": "condo"
        },
        {  # DTI exactly at 50% (high risk threshold)
            "credit_score": 710,
            "loan_amount": 250000,
            "property_value": 350000,
            "annual_income": 80000,
            "debt_amount": 40000,
            "loan_type": "fixed",
            "property_type": "single_family"
        }
    ]
}

INVALID_MORTGAGES = {
    "mortgages": [
        {  # Missing required fields (credit_score and loan_type)
            "loan_amount": 200000,
            "property_value": 300000,
            "annual_income": 80000,
            "debt_amount": 10000
        },
        {  # Invalid credit score (out of range)
            "credit_score": 900,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 70000,
            "debt_amount": 10000,
            "loan_type": "fixed",
            "property_type": "single_family"
        },
        {  # Negative values in non-allowed fields
            "credit_score": 650,
            "loan_amount": -150000,
            "property_value": 200000,
            "annual_income": 60000,
            "debt_amount": -5000,
            "loan_type": "fixed",
            "property_type": "condo"
        },
        {  # Invalid loan_type and property_type values
            "credit_score": 700,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 70000,
            "debt_amount": 10000,
            "loan_type": "variable",  # Invalid value
            "property_type": "townhouse"  # Invalid value
        }
    ]
}

AAA_MORTGAGES = {
    "mortgages": [
        {
            "credit_score": 800,
            "loan_amount": 150000,
            "property_value": 300000,
            "annual_income": 120000,
            "debt_amount": 5000,
            "loan_type": "fixed",
            "property_type": "single_family"
        },
        {
            "credit_score": 820,
            "loan_amount": 180000,
            "property_value": 350000,
            "annual_income": 150000,
            "debt_amount": 7000,
            "loan_type": "fixed",
            "property_type": "single_family"
        }
    ]
}

BBB_MORTGAGES = {
    "mortgages": [
        {
            "credit_score": 660,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 80000,
            "debt_amount": 25000,
            "loan_type": "adjustable",
            "property_type": "condo"
        },
        {
            "credit_score": 640,
            "loan_amount": 220000,
            "property_value": 275000,
            "annual_income": 85000,
            "debt_amount": 28000,
            "loan_type": "adjustable",
            "property_type": "condo"
        }
    ]
}

C_MORTGAGES = {
    "mortgages": [
        {
            "credit_score": 600,
            "loan_amount": 250000,
            "property_value": 250000,
            "annual_income": 60000,
            "debt_amount": 35000,
            "loan_type": "adjustable",
            "property_type": "condo"
        },
        {
            "credit_score": 620,
            "loan_amount": 280000,
            "property_value": 260000,
            "annual_income": 62000,
            "debt_amount": 40000,
            "loan_type": "adjustable",
            "property_type": "condo"
        }
    ]
}