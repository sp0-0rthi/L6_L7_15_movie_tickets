def parse_seat(seat):
    try:
        row = seat[0].upper()
        number = int(seat[1:])
    except (AttributeError, TypeError, IndexError, ValueError, OverflowError):
        return None
    return row, number

def total_price(prices_csv):
    try:
        prices = [int(p) for p in prices_csv.split(',')]
        total = round(sum(prices) * 1.18, 2)
    except (AttributeError, TypeError, ValueError, OverflowError):
        return None
    return total

def average_rating(ratings):
    try:
        values = [int(r) for r in ratings.split()]
        average = round(sum(values) / len(values), 1)
    except (AttributeError, TypeError, ValueError, ZeroDivisionError, OverflowError):
        return None
    return average

def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result if result is not None else "Invalid input")

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result if result is not None else "Invalid input")

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result if result is not None else "Invalid input")

if __name__ == "__main__":
    main()
