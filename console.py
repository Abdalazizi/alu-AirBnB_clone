"""
This module provides a few simple mathematical utility functions.
"""


def add_numbers(first_number: int, second_number: int) -> int:
    """
    Returns the sum of two integers.

    Args:
        first_number: The first number.
        second_number: The second number.
    
    Returns:
        The sum of the two numbers.
    """
    total = first_number + second_number
    return total


def calculate_average(numbers: list) -> float:
    """
    Calculates the average of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The average of the numbers. Returns 0 if the list is empty.
    """
    if not numbers:
        return 0.0

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average


def main():
    """
    This is the main function that demonstrates the math functions.
    """
    # Demonstrating the addition function
    number_1 = 5
    number_2 = 10
    sum_result = add_numbers(number_1, number_2)
    print(f"The sum of {number_1} and {number_2} is {sum_result}")

    # Demonstrating the average calculation
    my_list_of_numbers = [10, 20, 30, 40, 50]
    average_result = calculate_average(my_list_of_numbers)
    print(f"The average of {my_list_of_numbers} is {average_result}")


if __name__ == "__main__":
    main()