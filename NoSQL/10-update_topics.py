#!/usr/bin/env python3
"""
Module providing a function to update topics for a school document.
"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name.

    Args:
        mongo_collection: A pymongo collection object.
        name (str): The school name to update.
        topics (list): The list of topics approached in the school.
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)


if __name__ == "__main__":
    # This block will not be executed when imported
    pass 