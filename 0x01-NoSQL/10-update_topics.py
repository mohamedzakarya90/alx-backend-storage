#!/usr/bin/env python3
"""
Change the school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all the topics of  school
     document based on name

    -param mongo_collection:
    -param name:
    -param topics:
    -return:
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
