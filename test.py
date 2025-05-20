import random
import string
from checker import CorrectDoublyLinkedList
from main import DoublyLinkedList

def generate_random_inputs(num_strings=5000, length=100):
    """
    Generate a list of random strings.

    Args:
        num_strings (int): Number of strings to generate.
        length (int): Length of each string.

    Returns:
        List[str]: A list of random strings.
    """
    return [
        ''.join(random.choices(string.ascii_letters, k=length))
        for _ in range(num_strings)
    ]

def compare_lists(test_cases):
    mismatch_count = 0

    for idx, test in enumerate(test_cases, 1):
        # Create lists from both implementations
        dll_checker = CorrectDoublyLinkedList()
        dll_main = DoublyLinkedList()

        for char in test:
            dll_checker.insert(char)
            dll_main.insert(char)

        # Compare outputs
        str_checker = str(dll_checker)
        str_main = str(dll_main)

        is_pal_checker = dll_checker.is_custom_palindrome()
        is_pal_main = dll_main.is_custom_palindrome()

        if str_checker != str_main or is_pal_checker != is_pal_main:
            print(f"\n❌ Mismatch at test case #{idx}")
            print(f"Input: {test}")
            print(f"String (checker): {str_checker}")
            print(f"String (main):    {str_main}")
            print(f"Palindrome (checker): {is_pal_checker}")
            print(f"Palindrome (main):    {is_pal_main}")
            mismatch_count += 1

        if idx % 1000 == 0:
            print(f"✅ Checked {idx} test cases...")

    if mismatch_count == 0:
        print("\n🎉 All test cases matched successfully!")
    else:
        print(f"\n⚠️ {mismatch_count} mismatches found out of {len(test_cases)} test cases.")

if __name__ == "__main__":
    test_inputs = generate_random_inputs(num_strings=10000, length=10)
    compare_lists(test_inputs)
