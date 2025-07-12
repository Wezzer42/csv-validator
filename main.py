import csv, re, argparse, logging
from validate_row import Checkrow

logging.basicConfig(level=logging.INFO, filename="error_logs.log", filemode="w")

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
    parser.add_argument("--header", action="store_true", help="Threat first row as header.")
    args = parser.parse_args()
    default_input = "default_input.csv"
    default_output = "default_output.csv"
    if args.input:
        if args.output:
            write_csv(args.input, args.output, args.header)
        else:
            write_csv(args.input, default_output, args.header)
    else:
        if args.output:
            write_csv(default_input, args.output, args.header)
        else:
            write_csv(default_input, default_output, args.header)
            
if __name__ == "__main__":
    main()