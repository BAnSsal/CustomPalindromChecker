class Node:
    """
    Node class for doubly linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CorrectDoublyLinkedList:
    """
    Custom implementation of doubly linked list for character storage
    with custom palindrome detection
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert(self, char):
        """
        Insert a character at the end of the list in O(1) time
        
        Args:
            char: A single character to insert
        """
        # Create a new node
        new_node = Node(char)
        
        # If list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node to the end
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def is_custom_palindrome(self):
        """
        Check if the list forms a custom palindrome:
        - Ignoring case
        - Ignoring vowels (a, e, i, o, u)
        - Ignoring consecutive repeating characters
        
        Returns:
            bool: True if the list is a custom palindrome, False otherwise
        """
        if self.head is None:
            return True  # Empty list is a palindrome
        
        # Process the list to get characters according to custom rules
        processed = []
        current = self.head
        prev_char = None
        
        while current:
            char = current.data.lower()  # Convert to lowercase
            
            # Skip if vowel
            if char in {'a', 'e', 'i', 'o', 'u'}:
                current = current.next
                continue
                
            # Skip if consecutive repetition
            if char == prev_char:
                current = current.next
                continue
                
            processed.append(char)
            prev_char = char
            current = current.next
        
        # Check if processed characters form a palindrome
        left = 0
        right = len(processed) - 1
        
        while left < right:
            if processed[left] != processed[right]:
                return False
            left += 1
            right -= 1
            
        return True
    
    def __str__(self):
        """
        Return a string representation of the list
        
        Returns:
            str: The characters in the list as a string
        """
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
            
        return ''.join(result)


def main():
    """
    Driver function to test the DoublyLinkedList implementation
    """
    test_cases = ["Deified", "ddoodd", "banana"]
    
    for test in test_cases:
        print(f"\nTesting: {test}")
        
        # Create a new list
        dll = CorrectDoublyLinkedList()
        
        # Insert each character
        for char in test:
            dll.insert(char)
            
        # Check if it's a custom palindrome
        is_palindrome = dll.is_custom_palindrome()
        
        # Get the processed characters for debugging
        processed = []
        current = dll.head
        prev_char = None
        while current:
            char = current.data.lower()
            if char not in {'a', 'e', 'i', 'o', 'u'} and char != prev_char:
                processed.append(char)
                prev_char = char
            current = current.next
        
        print(f"List content: {dll}")
        print(f"Is custom palindrome: {is_palindrome}")
        print(f"Processed characters: {processed}")

if __name__ == "__main__":
    main()
