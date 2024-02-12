#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/12 19:20
# @Author  : frank yang
# @File    : remove_linked_list_elements.py
# @IDE     : PyCharm
from typing import Optional

from algorithm.ListNode.list_node import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=None, next_node=None):
#         self.val = val
#         self.next = next_node
class RemoveElements:

    @staticmethod
    def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next_node=head)
        pre_head = dummy
        while pre_head and pre_head.next:
            if pre_head.next.val == val:
                pre_head.next = pre_head.next.next
            else:
                pre_head = pre_head.next
        return dummy.next


if __name__ == "__main__":
    head = [1, 2, 6, 3, 4, 5, 6]
    test_data = ListNode.array_to_list(head)

    res_node = RemoveElements.remove_elements(test_data, 6)

    head_validate = [1, 2, 3, 4, 5]
    test_validate = ListNode.array_to_list(head_validate)

    assert res_node.compare(test_validate) is True
