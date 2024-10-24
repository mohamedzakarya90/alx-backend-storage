#!/usr/bin/env python3
"""
inserting document in python
"""


def insert_school(mongo_collection, **kwargs):
    """
     inserting new document in 
      collection based on kwargs

    -param mongo_collection:
    -param kwargs:
    -return:
    """
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
