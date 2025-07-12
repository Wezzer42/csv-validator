import re, logging

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
