#!/usr/bin/env python3

"""
python function that returns the list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    schools_by_topic: returns the list of schools having a specific topic

    Args:
        mongo_collection: Mongosb collection
        topic: topic to search for

    Return:
        list: A list of school documents having the specified topic
    """

    return list(mongo_collection.find({"topics": topic}))
