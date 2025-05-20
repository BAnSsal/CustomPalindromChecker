# Custom Palindrome Checker

## 🧩 Problem Summary

Given a string, determine if it is a **custom palindrome** using a doubly linked list. A **custom palindrome** is defined with the following conditions:
- It should be **case-insensitive**
- **Vowels** (`a`, `e`, `i`, `o`, `u`) are ignored
- **Consecutive repeating characters** are considered as one and ignored in the comparison

---

## 🚀 Approach Used

- A **custom doubly linked list** is implemented from scratch using `Node` and `DoublyLinkedList` classes.
- Each character is inserted into the linked list.
- The list is traversed from both ends (`head` and `tail`) while skipping:
  - Vowels
  - Repeated consecutive characters
- Characters are compared case-insensitively until the pointers cross.
- The logic is implemented in `is_custom_palindrome()` function.
- We compare the outputs of two implementations:
  - `main.py` (student's implementation)
  - `checker.py` (correct version)
  using `test.py`.

---

## ⏱ Time & Space Complexity

### Insertion:
- **Time Complexity:** O(1) per character → O(n) total for string of length n
- **Space Complexity:** O(n) for storing n characters in the linked list

### Custom Palindrome Check:
- **Time Complexity:** O(n) in worst-case (single pass from both ends)
- **Space Complexity:** O(1) extra (excluding the list storage)

---

## ✅ Sample Test Cases

| Input           | Linked List | Is Custom Palindrome? |
|----------------|-------------|------------------------|
| `Deified`       | D → e → i → f → i → e → d | ✅ `True` |
| `ddoodd`        | d → d → o → o → d → d      | ✅ `True` |
| `banana`        | b → a → n → a → n → a      | ❌ `False` |
| `WoUbfKFFbW`    | W → o → U → b → f → K → F → F → b → W | ✅ `True` |
| `racecar`       | r → a → c → e → c → a → r | ✅ `True` |
| `aabbccddeeff`  | a → a → b → b → c → c → d → d → e → e → f → f | ❌ `False` |

---

## 📁 Files

- `main.py` — Your implementation of the custom doubly linked list
- `checker.py` — Reference implementation used for comparison
- `test.py` — Testing 10,000 random strings and comparing both implementations
