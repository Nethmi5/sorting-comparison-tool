import time
import random
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

def generate_random_list(size=10, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def main():
    data = []
    results = {}

    while True:
        print("\n--- Data Sorter: Sorting Algorithm Comparison Tool ---")
        print("1. Enter numbers manually")
        print("2. Generate random numbers")
        print("3. Perform Bubble Sort")
        print("4. Perform Merge Sort")
        print("5. Perform Quick Sort")
        print("6. Compare all algorithms (show performance table)")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            raw = input("Enter numbers separated by spaces: ")
            data = [int(x) for x in raw.split()]
        elif choice == '2':
            size = int(input("Enter size of dataset: "))
            data = generate_random_list(size)
            print("Generated List:", data)
        elif choice in ['3', '4', '5']:
            if not data:
                print("No data available. Please enter or generate numbers first.")
                continue

            algo = {'3': 'Bubble Sort', '4': 'Merge Sort', '5': 'Quick Sort'}[choice]
            func = {'3': bubble_sort, '4': merge_sort, '5': quick_sort}[choice]

            start = time.perf_counter()
            sorted_data, steps = func(data)
            duration = time.perf_counter() - start

            results[algo] = (duration, steps)

            print(f"\n{algo} Result:")
            print("Sorted List:", sorted_data)
            print(f"Execution Time: {duration:.6f} seconds")
            print(f"Steps Count: {steps}")
        elif choice == '6':
            if not results:
                print("No results to compare yet.")
                continue
            print("\n--- Comparison Table ---")
            print(f"{'Algorithm':<15}{'Time (s)':<15}{'Steps'}")
            for algo, (t, s) in results.items():
                print(f"{algo:<15}{t:<15.6f}{s}")
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
