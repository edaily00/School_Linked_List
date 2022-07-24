class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self._head = None

    def get_head(self):
        return self._head


    def rec_add(self, val, current):

        if self._head is None:
            self._head = Node(val)

        elif current.next is None:
            current.next = Node(val)

        elif current.next is not None:
            current = current.next
            return self.rec_add(val, current)

    def add(self, val):
        self.rec_add(val, self._head)

    def rec_display(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.rec_display(node.next)

    def display(self):

        self.rec_display(self._head)

    def rec_remove(self, val, previous, current):

        if self._head is None:
            return

        if current is None:
            return

        if self._head.data == val:
            self._head = self._head.next

        if current is not None and current.data != val:
            previous = current
            current = current.next
            return self.rec_remove(val, previous, current)

        if current is not None and current.data == val:
            previous.next = current.next


    def remove(self, val):

        self.rec_remove(val, 0, self._head)

    def is_empty(self):
        return self._head is None

    def rec_contains(self, val, current):

        if current is None:
            return False

        if current.data == val:
            return True
        else:
            return self.rec_contains(val, current.next)


    def contains(self, value):
        return self.rec_contains(value, self._head)

    def rec_insert(self, val, pos, previous, current, current_pos):

        if current.next == None:
            self.add(val)
            return
        if pos == current_pos:
            new = Node(val)
            temp = current
            current = new
            previous.next = current
            current.next = temp
            return

        if pos != current_pos:
            current_pos += 1
            return self.rec_insert(val, pos, current, current.next, current_pos)


    def insert(self, val, pos):
        self.rec_insert(val, pos, 0, self._head, 0)

    def rec_reverse(self, current):
        if current is None or current.next is None:
            return current

        new_head = self.rec_reverse(current.next)
        current.next.next = current
        current.next = None

        return new_head


    def reverse(self):
        self._head = self.rec_reverse(self._head)
    #def insert(self, value, pos):

    def to_plain_list_helper(self,the_list, current):

        if current is None:
            return
        the_list.append(current.data)
        self.to_plain_list_helper(the_list, current.next)

        return the_list


    def to_plain_list(self):

        the_list = []
        return self.to_plain_list_helper(the_list, self._head)


"""hey"""