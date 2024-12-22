#!/usr/bin/env python3

"""
Python function that unserts a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    insert_school: insert a set of values as document
                    into collection

    Args:
        mongo_collection: mongo db collection
        kwargs: the collection of args to save

    Return: id of inserted content
    """
    mongo_collection.delete_many({})
    return mongo_collection.insert_one(kwargs).inserted_id
    
