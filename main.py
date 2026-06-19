def check_even(number: int) -> bool:
    # Notice no curly braces! Indentation matters.
    if number % 2 == 0:
        return True
    else:
        return False

test_num: int = 42
print(f"Is {test_num} even? {check_even(test_num)}")