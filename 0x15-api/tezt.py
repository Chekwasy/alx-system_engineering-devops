#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/user/2"
    al = requests.get(url, params={"userId": 2}).json()
    print(al)
