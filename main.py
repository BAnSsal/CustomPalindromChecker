class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
   
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert(self, char):
        #  Insert  character O(1)
        
        new_node = Node(char)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1

    def is_custom_palindrome(self):
            """
            Check if the list forms a custom palindrome:
            - Ignoring case
            - Ignoring {'a', 'e', 'i', 'o', 'u'} (a, e, i, o, u)
            - Ignoring consecutive repeating characters
            
            Returns:
                bool: True if the list is a custom palindrome, False otherwise
            """
            if self.head is None:
                return True  # Empty list is a palindrome
                
            start = self.head
            end = self.tail
            
                        # Main loop for checking palindrome
            while start is not None and end is not None and start != end and start.prev != end:
                # advance start to next _valid_ character
                while start is not None and (
                    start.data.lower() in {'a', 'e', 'i', 'o', 'u'}
                    or (start.prev and start.data.lower() == start.prev.data.lower())
                ):
                    start = start.next

                # advance end to previous _valid_ character
                while end is not None and (
                    end.data.lower() in {'a', 'e', 'i', 'o', 'u'}
                    or (end.next and end.data.lower() == end.next.data.lower())
                ):
                    end = end.prev

                # once both are on valid chars, check if they've crossed
                if start is None or end is None or start == end or start.prev == end:
                    return True

                # compare
                if start.data.lower() != end.data.lower():
                    return False

                # move inwards
                start = start.next
                end   = end.prev

                            
                        
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
    test_cases = ["uVrviRvovV", "WoUbfKFFbW", "banana"]
    
    for test in test_cases:
        print(f"\nTesting: {test}")
        
        # Create a new list
        dll = DoublyLinkedList()
        
        # Insert each character
        for char in test:
            dll.insert(char)
            
        # Check if it's a custom palindrome in O(1) time
        is_palindrome = dll.is_custom_palindrome()
        
        print(f"List content: {dll}")
        print(f"Is custom palindrome: {is_palindrome}")
        


if __name__ == "__main__":
    main()