import logging

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        try:
            new_node = Node(value)
            if self.root is None:
                self.root = new_node
            else:
                current_node = self.root
                while True:
                    if value < current_node.value:
                        if current_node.left is None:
                            current_node.left = new_node
                            break
                        else:
                            current_node = current_node.left
                    else:
                        if current_node.right is None:
                            current_node.right = new_node
                            break
                        else:
                            current_node = current_node.right
        except Exception as e:
            logging.error(f"Error in insert: {e}")
            return "An error occurred during insert in binary search tree: {}".format(str(e))

    def search(self, value):
        try:
            current_node = self.root
            while current_node is not None:
                if value == current_node.value:
                    return True
                elif value < current_node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            return False
        except Exception as e:
            logging.error(f"Error in search: {e}")
            return "An error occurred during search in binary search tree: {}".format(str(e))

    def in_order_traversal(self, node, result):
        try:
            if node is not None:
                self.in_order_traversal(node.left, result)
                result.append(node.value)
                self.in_order_traversal(node.right, result)
        except Exception as e:
            logging.error(f"Error in in_order_traversal: {e}")
            return "An error occurred during in order traversal in binary search tree: {}".format(str(e))

    def get_in_order_traversal(self):
        try:
            result = []
            self.in_order_traversal(self.root, result)
            return result
        except Exception as e:
            logging.error(f"Error in get_in_order_traversal: {e}")
            return "An error occurred during in order traversal in binary search tree: {}".format(str(e))
