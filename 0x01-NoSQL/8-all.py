#!/usr/bin/env python3
"""
Listing all the documents in python
"""


def list_all(mongo_collection):
    """
    listing all documents in collection

    -param mongo_collection:
    -return:
    """
    return mongo_collection.find()
