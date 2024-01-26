#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/1/26 15:24
# @Author  : frank yang
# @File    : create_PR.py
# @IDE     : PyCharm\

import argparse
import json

import requests


def __init__():
    parser = argparse.ArgumentParser(description="Create the PR automatic")
    parser.add_argument(name_or_flags=('-t', '--title'), help="input the title of PR", required=True)
    parser.add_argument(name_or_flags=('-m', '--message'), help='input the PR message', required=True)
    return parser.parse_args()


def create_pr_on_gitee(title: str, body: str):
    """
    create a Pull Request on Gitee
    :param title: Pull Request标题
    :param body: Pull Request描述（可选）
    """
    owner = "frankyang92"
    repo = "frankyang92"


    url = f"https://gitee.com/api/v5/repos/{owner}/{repo}/pulls"

    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "access_token": get_gitee_access_token(),
        "base": "master",
        "head": "develop",
        "title": title,
        "body": body,
        "squash": True  # 设置为False，如果想要立即公开Pull Request
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    return response.status_code


def get_gitee_access_token():
    """
    Token from the Gitee
    """
    token = ""
    with open("MyToken.txt") as token:
        token = token.readlines()
    return token


if __name__ == "__main__":
    args = __init__()
    create_pr_on_gitee(args.t, args.m)
