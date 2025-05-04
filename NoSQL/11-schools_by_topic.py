#!/usr/bin/env python3
"""
Module providing a function to find schools by topic.
"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic searched.

    Returns:
        A list of documents (schools) that have the specified topic.
    """
    query = {"topics": topic}
    schools = mongo_collection.find(query)
    return list(schools)


if __name__ == "__main__":
    # This block will not be executed when imported
    pass 