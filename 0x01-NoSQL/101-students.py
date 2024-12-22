#!/usr/usr/bin/env python3

"""
Python function that returns all stuents sorted by average score
"""


def top_students(mongo_collection):
    """
    top_students: returns all students sorted by average score

    Args:
        mongo_collection: mongoClient collection

    Return:
        list of all students sorted by average score
    """

    return list(mongo_collection.aggregate(
            [
                {"$unwind": "$topics"},
                {"$group":
                 {"_id": "$_id",
                  "name": {"$first": "$name"},
                  "averageScore": {"$avg": "$topics.score"}
                    }},

                 {"$sort": {"averageScore": -1}}
                ]
            ))
    
