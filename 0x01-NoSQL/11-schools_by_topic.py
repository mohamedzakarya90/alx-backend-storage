#!/usr/bin/env python3
"""
where can i learn python
"""


def schools_by_topic(mongo_collection, topic):
    """
     returning the list of school which having a specific topic

    -param mongo_collection:
    -param topic:
    -return:
    """
    return mongo_collection.find({"topics": topic})
