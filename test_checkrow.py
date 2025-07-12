from main import Checkrow
import pytest

def test_valid_row():
    row = ["John Doe", "john@example.com", "30"]
    cr = Checkrow(row, 1)
    assert cr.check_row() == True

def test_invalid_email():
    row = ["John Doe", "invalid_email", "30"]
    cr = Checkrow(row, 2)
    assert cr.check_row() == False

def test_invalid_age():
    row = ["John Doe", "john@example.com", "999"]
    cr = Checkrow(row, 3)
    assert cr.check_row() == False

def test_empty_name():
    row = ["", "john@example.com", "30"]
    cr = Checkrow(row, 4)
    assert cr.check_row() == False

def test_empty_row():
    row = []
    cr = Checkrow(row, 5)
    assert cr.check_row() == False

def test_row_with_extra_columns():
    row = ["John", "john@example.com", "30", "extra"]
    cr = Checkrow(row, 6)
    assert cr.check_row() == False
