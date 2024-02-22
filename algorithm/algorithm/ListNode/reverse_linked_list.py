#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/22 11:10
# @Author  : frank yang
# @File    : reverse_linked_list.py
# @IDE     : PyCharm
from typing import Optional

from algorithm.ListNode.list_node import ListNode


class ReverseLinkedList:
    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre


if __name__ == "__main__":
    test_data = [1, 2, 3, 4, 5]
    head = ListNode.array_to_list(test_data)

    res_node = ReverseLinkedList.reverse_list(head)

    head_validate = [5, 4, 3, 2, 1]
    test_validate = ListNode.array_to_list(head_validate)
    assert res_node.compare(test_validate) is True
