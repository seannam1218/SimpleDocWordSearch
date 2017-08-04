class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def count_node(self, data):
        node = self.cur_node
        total = 0
        while node:
            if node.data == data:
                total += 1
            node = node.next
        return total


    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print ("found: " + str(node.data))
            node = node.next
