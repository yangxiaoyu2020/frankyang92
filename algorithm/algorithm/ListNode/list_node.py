#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/12 19:21
# @Author  : frank yang
# @File    : list_node.py
# @IDE     : PyCharm


class Node:
    def __init__(self):
        self.val = None


class ListNode(Node):
    def __init__(self, val=None, next_node=None):
        super().__init__()
        self.val = val
        self.next = next_node

    def compare(self, another_list_node):
        while self and another_list_node:
            if self.val != another_list_node.val:
                return False
            self = self.next
            another_list_node = another_list_node.next
        # Check if both lists have been traversed completely
        return True

    @staticmethod
    def array_to_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    # Example usage


if __name__ == "__main__":
    # Creating two linked lists
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)

    list2 = ListNode(1)
    list2.next = ListNode(2)
    list2.next.next = ListNode(3)

    # Comparing the two lists
    list1.compare(list2)
