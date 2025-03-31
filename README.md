
# Mortgage Credit Rating System
## Overview

This project is to implement the credit rating calculation logic for residential mortgage-backed
securities (RMBS). The system processes mortgage data from a JSON file, calculates risk scores, and determines the final credit rating (AAA, BBB, or C).


## Features

- **Mortgage Validation**: Ensures all input mortgage data follows predefined constraints using Pydantic.

- **Risk Factor Calculation**: Computes risk based on LTV (Loan-to-Value), DTI (Debt-to-Income), Credit Score, Loan Type, and Property Type.

- **Efficient Computation**: Supports batch processing using Pandas for scalability.

- **Error Handling & Logging**: Catches validation errors and unexpected exceptions.

- **Unit Testing**: Validates correctness and edge cases using unittest.


## Tech Stack

**Python** 

**Pydantic:** Ensures mortgage data adheres to defined constraints, preventing malformed inputs from being processed.

**Pandas:** For optimized data processing and to handle a large number of mortgages efficiently

**Logging:** The system logs all validation errors and unexpected exceptions for debugging.

**Unittest:** For testing different test cases and scenarios.


## Project Structure

```
├── credit_rating.py      # Main script for credit rating calculation
├── models.py             # Defines Mortgage and MortgageInput models
├── utils.py              # Utility functions for risk calculations
├── test_credit_rating.py # Unit tests for validation and credit rating
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```


## Installation & Setup

1. Clone the Repository

```
  git clone https://github.com/vikaspadhi/crisil_assignment.git
  cd crisil_assignment
```

2. Install Dependencies

```bash
  pip install -r requirements.txt
```

3. Run the Credit Rating Calculation

```bash
  python credit_rating.py payload.json
``` 
Where payload.json is a valid JSON file containing mortgage details.



## Running Tests

To run tests, run the following command

```bash
  python -m unittest test_credit_rating.py
```

