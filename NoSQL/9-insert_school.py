#!/usr/bin/env python3
"""
Module providing a function to insert a document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Keyword arguments representing the document's fields and values.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id


if __name__ == "__main__":
    # This block will not be executed when imported
    pass 