import csv, re, argparse, logging


logging.basicConfig(level=logging.INFO, filename="error_logs.log", filemode="w")

class Checkrow:
    def __init__(self, row, row_number):
        self.row_number = row_number
        self.row_valid = self.validate_row(row)
        if self.row_valid:
            self.name = row[0]
            self.email = row[1]
            self.age = row[2]
        
    def validate_row(self, row):
        if not row:
            logging.info(f"In row {self.row_number} has errors: row empty")
            return False
        if len(row) != 3:
            logging.info(f"In row {self.row_number} has errors: row length not valid")
            return False
        return True

    def check_row(self):
        if not self.row_valid:
            return False

        errors = []

        if self.check_name() != True:
            errors.append(self.check_name())

        if self.check_email() != True:
            errors.append(self.check_email())

        if self.check_age() != True:
            errors.append(self.check_age())

        if errors:
            logging.info(f"In row {self.row_number} has errors: {errors}")
            return False
        else:
            return True

    def check_name(self):
        return True if self.name else "NAME_INVALID"
    
    def check_email(self):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return True if re.match(pattern, self.email) else "INVALID_EMAIL"
    
    def check_age(self):
        try:
            int_age = int(self.age)
        except ValueError:
            return "VALUE_ERROR"
        return True if 0 < int_age < 120 else "OUT_OF_RANGE"


def process_csv_row(filename, headers):
    with open(filename, 'r', newline='') as csvfile:
        data = csv.reader(csvfile)
        output_data = []
        if headers:
            output_data.append(next(data))
            start_index = 2
        else:
            start_index = 1
        for i, row in enumerate(data, start_index):
            raw = Checkrow(row, i)
            checked = raw.check_row()
            if checked:
                output_data.append(row)
        return output_data
    
def write_csv(fileinput, fileoutput, headers):
    data = process_csv_row(fileinput, headers)
    with open(fileoutput, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

   
    
def main():
    parser = argparse.ArgumentParser(description="A script for checking name, email and age from csv.")
    parser.add_argument("--input",type=str,help="Path to input csv file")
    parser.add_argument("--output",type=str,help="Path to output csv file")
    parser.add_argument("--headers", action="store_true", help="Threat first row as header.")
    args = parser.parse_args()
    default_input = "default_input.csv"
    default_output = "default_output.csv"
    if args.input:
        if args.output:
            write_csv(args.input, args.output, args.headers)
        else:
            write_csv(args.input, default_output, args.headers)
    else:
        if args.output:
            write_csv(default_input, args.output, args.headers)
        else:
            write_csv(default_input, default_output, args.headers)
            
if __name__ == "__main__":
    main()