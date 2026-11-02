import pytest
from movie_tickets import ticket_price, group_discount, snack_combo

# Branch coverage test cases - Spoorthi A N, PES2UG24CS515
# Each decision (if / elif / or) is exercised on BOTH its True and False sides.

# --- ticket_price: invalid input branches ---
def test_unknown_seat():
    with pytest.raises(ValueError):
        ticket_price("balcony", 25, 15, False)

def test_show_hour_too_low():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, -1, False)

def test_show_hour_too_high():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, 24, False)

# --- ticket_price: show-time branches (morning / afternoon / evening) ---
def test_early_morning_boundary():
    assert ticket_price("regular", 25, 0, False) == 100   # show_hour < 12 True

def test_noon_boundary():
    assert ticket_price("regular", 25, 12, False) == 150  # show_hour < 12 False, >= 18 False

def test_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150

def test_evening_boundary():
    assert ticket_price("regular", 25, 18, False) == 180  # show_hour >= 18 True

def test_late_night_boundary():
    assert ticket_price("regular", 25, 23, False) == 180

# --- ticket_price: weekend branch both ways ---
def test_weekend_evening():
    assert ticket_price("regular", 25, 19, True) == 220   # is_weekend True

def test_weekday_evening():
    assert ticket_price("regular", 25, 19, False) == 180  # is_weekend False

# --- ticket_price: age branches (toddler / child / adult / senior) ---
def test_toddler_free():
    assert ticket_price("regular", 2, 15, False) == 0     # age < 3 True

def test_child_boundary():
    assert ticket_price("regular", 3, 15, False) == 75    # age < 3 False, age <= 12 True

def test_adult_lower_boundary():
    assert ticket_price("regular", 13, 15, False) == 150  # age <= 12 False, age >= 60 False

def test_adult_upper_boundary():
    assert ticket_price("regular", 59, 15, False) == 150

def test_senior_boundary():
    assert ticket_price("regular", 60, 15, False) == 75   # age >= 60 True

def test_senior_premium():
    assert ticket_price("premium", 65, 15, False) == 125

def test_child_premium_morning_weekend():
    assert ticket_price("premium", 10, 10, True) == 120   # combined branches

def test_senior_recliner_evening_weekend():
    assert ticket_price("recliner", 70, 20, True) == 235

# --- group_discount: every discount tier and the student short-circuit ---
def test_no_tickets():
    with pytest.raises(ValueError):
        group_discount(0, False)

def test_single_ticket():
    assert group_discount(1, False) == 0

def test_small_group_student_no_discount():
    assert group_discount(2, True) == 0    # student but discount == 0, so no +5

def test_medium_group_boundary():
    assert group_discount(5, False) == 10  # tickets >= 5 True, >= 10 False

def test_medium_group_student():
    assert group_discount(7, True) == 15

def test_large_group_boundary():
    assert group_discount(10, False) == 15  # tickets >= 10 True

def test_large_group_student():
    assert group_discount(12, True) == 20

# --- snack_combo: all sizes, coupon both ways ---
def test_small_combo():
    assert snack_combo("small", False) == 120

def test_small_combo_coupon():
    assert snack_combo("small", True) == 70

def test_medium_combo():
    assert snack_combo("medium", False) == 180

def test_medium_combo_coupon():
    assert snack_combo("medium", True) == 130

def test_large_combo():
    assert snack_combo("large", False) == 250

def test_large_combo_coupon():
    assert snack_combo("large", True) == 200
