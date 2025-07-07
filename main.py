class Node:
    """Class to represent a single node in the linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class to represent the singly linked list"""
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        """Add a node to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all elements of the list"""
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index) from the list"""
        try:
            if not self.head:
                raise Exception("Cannot delete from an empty list.")

            if n <= 0:
                raise IndexError("Index must be a positive integer (1-based).")

            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node with data: {deleted_data}")
                return

            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError("Index out of range.")

            deleted_data = current.next.data
            current.next = current.next.next
            print(f"Deleted node with data: {deleted_data}")

        except Exception as e:
            print("Error:", e)


# ----------- Testing the LinkedList class -----------

# Create the linked list
ll = LinkedList()

# Add sample nodes
ll.add_to_end(10)
ll.add_to_end(20)
ll.add_to_end(30)
ll.add_to_end(40)

print("Initial list:")
ll.print_list()

# Delete the 2nd node
print("\nDeleting 2nd node:")
ll.delete_nth_node(2)
ll.print_list()

# Delete 1st node
print("\nDeleting 1st node:")
ll.delete_nth_node(1)
ll.print_list()

# Try deleting an out-of-range node
print("\nDeleting 10th node (should raise error):")
ll.delete_nth_node(10)

# Try deleting from an empty list
print("\nDeleting all remaining nodes:")
ll.delete_nth_node(1)
ll.delete_nth_node(1)

print("\nTrying to delete from empty list:")
ll.delete_nth_node(1)