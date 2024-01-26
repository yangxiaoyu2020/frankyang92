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


def init_args():
    parser = argparse.ArgumentParser(description="Create the PR automatic")
    parser.add_argument('-t', '--title', help="input the title of PR", required=True,  dest='title')
    parser.add_argument('-m', '--message', help='input the PR message', required=True, dest='message')
    return parser.parse_args()

def create_body(message: str) -> str:
    body = f'''
    ### Description: 
    
    ### Changelog:
    
    * {message.replace("_", " ")}
    
    ### Test
    
    -[x] Pass the test
    '''
    return body

def create_pr_on_gitee(title: str, message: str)-> str:
    """
    create a Pull Request on Gitee
    :param title: Pull Request title
    :param message: Pull Request message
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
        "title": title.replace("_", " "),
        "body": create_body(message=message),
        "squash": True  # 设置为False，如果想要立即公开Pull Request
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    return response.status_code


def get_gitee_access_token():
    """
    Token from the Gitee
    """
    token = ""
    with open("MyToken.txt") as token:
        token = token.readlines()
    print(token[0])
    return token[0]


if __name__ == "__main__":
    args = init_args()
    create_pr_on_gitee(args.title, args.message)
