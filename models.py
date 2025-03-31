from pydantic import BaseModel,Field,field_validator
from enum import Enum

class LoanType(str,Enum):
    fixed = 'fixed'
    adjustable = 'adjustable'
    
class PropertyType(str,Enum):
    single_family="single_family"
    condo="condo"

class Mortgage(BaseModel):
    '''
    This pydantic class is used to validate the mortgage format.
    '''
    credit_score:int = Field(ge=300,le=850,description="Credit score must be between 300 and 850")
    loan_amount:float = Field(ge=0,description="Loan amount must be greater than 0")
    property_value:float = Field(gt=0,description="Property value must be greater than 0")
    annual_income: float =Field(gt=0,description="Annual income must be greater than 0")
    debt_amount:float = Field(ge=0,description="Debt amount must be greater than 0")
    loan_type: LoanType  = Field(description="Loan type must be fixed or adjustable")
    property_type:PropertyType = Field(description="Property type must be single_family or condo")
    
class MortgageInput(BaseModel):
    '''
    Model to validate list of mortgages.
    '''
    mortgages:list[Mortgage]
    
    @field_validator("mortgages")
    def validate_mortgages(cls,v):
        if not v:
            raise ValueError("The mortgages list can not be empty")
        return v