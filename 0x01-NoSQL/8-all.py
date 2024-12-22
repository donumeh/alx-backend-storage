#!/usr/bin/env python3
"""
Write a python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    list_all: lists all documents in a collection

    args:
        mongo_collection: MongoClient()

    Return:empty list if no docuent else list of document
    """

    return mongo_collection.find()

