import random
import time

# ----------------------------------------------------------
# Utility Functions for Data Sorter Project
# ----------------------------------------------------------

def generate_random_list(size=10, min_val=1, max_val=100):
    """
    Generates a list of random integers.
    :param size: Number of elements in the list
    :param min_val: Minimum possible value
    :param max_val: Maximum possible value
    :return: A list of random integers
    """
    return [random.randint(min_val, max_val) for _ in range(size)]


def validate_integer_input(prompt, min_value=None, max_value=None):
    """
    Prompts user for integer input with optional range validation.
    :param prompt: The text displayed to the user
    :param min_value: Minimum allowed value (optional)
    :param max_value: Maximum allowed value (optional)
    :return: A valid integer input
    """
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def time_algorithm(func, data):
    """
    Measures execution time and steps for a given sorting algorithm.
    :param func: Sorting function (e.g., bubble_sort)
    :param data: List of numbers to sort
    :return: (sorted_data, elapsed_time, steps)
    """
    start = time.perf_counter()
    sorted_data, steps = func(data)
    elapsed = time.perf_counter() - start
    return sorted_data, elapsed, steps


def display_comparison_table(results):
    """
    Displays a formatted performance comparison table for all algorithms.
    :param results: Dictionary {algorithm_name: (time, steps)}
    """
    if not results:
        print("\nNo results available. Run sorting algorithms first.")
        return

    print("\n--- Sorting Algorithm Performance Comparison ---")
    print(f"{'Algorithm':<15}{'Time (seconds)':<20}{'Steps/Operations'}")
    print("-" * 55)
    for algo, (t, steps) in results.items():
        print(f"{algo:<15}{t:<20.6f}{steps}")
    print("-" * 55)


def display_list(title, data):
    """
    Prints a list with a given title in a neat format.
    :param title: Description (e.g., "Original List" or "Sorted List")
    :param data: List of numbers
    """
    print(f"\n{title}:")
    print("[" + ", ".join(map(str, data)) + "]")
