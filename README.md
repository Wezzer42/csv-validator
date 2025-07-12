# CSV Validator

## Description

This script validates rows of a CSV file containing user data against the following criteria:

- Exactly 3 columns: `name`, `email`, `age`
- Name must be non-empty
- Email must match a valid format (using regex)
- Age must be an integer between 1 and 119

All validation errors are logged to `error_logs.log`.

---

## How to Run

Requires Python 3.6+.

1. No extra dependencies are needed (only standard libraries).

2. Run the script:

bash
python main.py --input input.csv --output output.csv --header
Arguments
Argument	Description
--input	Path to the input CSV file
--output	Path to the output CSV file containing valid rows
--header	Indicates that the first row is a header

If arguments are omitted, defaults are used:

default_input.csv

default_output.csv

## Example Run
bash
Copy
Edit
python main.py --input users.csv --output clean_users.csv --header
After execution:

All valid rows will be written to clean_users.csv.

Validation errors will be recorded in error_logs.log with row numbers and error types.

## Testing
This project includes tests written with pytest.

To run tests:

bash
Copy
Edit
pytest
The tests cover:

A valid row

Invalid email

Invalid age

Empty name

Empty row

Row with extra columns

##  Example Logs
Example contents of error_logs.log:

less
Copy
Edit
In row 3 has errors: ['INVALID_EMAIL']
In row 5 has errors: ['NAME_INVALID', 'VALUE_ERROR']
🛠 Possible Improvements
Add support for different delimiters (e.g., ;)

Allow configuration via YAML or JSON

Generate a detailed report summarizing validation results

Print errors to the console (--verbose flag)

Package as a Python module (pip install .)