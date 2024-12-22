#!/usr/bin/env python3

"""
Python function that chages all topics of a school doc
"""

def update_topics(mongo_collection, name, topics):
    """
    update_topics: changes all topcis of a school document

    Args:
        mongo_collection: the mongo collection
        name: the key value to change
        topics: the new values of key

    Return: None
    """
    item_topics = mongo_collection.find_one({"name": name})

    if item_topics.get('topics') != topics:
        mongo_collection.update_one({"name":name}, {"$set": {"topics": topics}})

