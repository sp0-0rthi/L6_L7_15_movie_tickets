import pytest
from movie_tickets import ticket_price, group_discount, snack_combo

# Code coverage test cases - Spoorthi A N, PES2UG24CS515

def test_unknown_seat():
    with pytest.raises(ValueError):
        ticket_price("balcony", 25, 15, False)

def test_invalid_show_hour():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, -1, False)

def test_morning_weekday_adult():
    assert ticket_price("regular", 25, 10, False) == 100

def test_afternoon_weekday_adult():
    assert ticket_price("regular", 25, 15, False) == 150

def test_evening_weekend_adult():
    assert ticket_price("regular", 25, 19, True) == 220

def test_child_ticket():
    assert ticket_price("regular", 5, 15, False) == 75

def test_toddler_free():
    assert ticket_price("regular", 2, 15, False) == 0

def test_senior_premium():
    assert ticket_price("premium", 65, 15, False) == 125

def test_no_tickets():
    with pytest.raises(ValueError):
        group_discount(0, False)

def test_small_group():
    assert group_discount(2, False) == 0

def test_medium_group():
    assert group_discount(7, False) == 10

def test_large_group():
    assert group_discount(12, False) == 15

def test_student_group():
    assert group_discount(12, True) == 20

def test_small_combo():
    assert snack_combo("small", False) == 120

def test_medium_combo_coupon():
    assert snack_combo("medium", True) == 130

def test_large_combo():
    assert snack_combo("large", False) == 250
