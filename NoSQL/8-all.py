#!/usr/bin/env python3
"""
Module providing a function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list containing all documents in the collection,
        or an empty list if the collection is empty.
    """
    documents = mongo_collection.find()
    return list(documents)


if __name__ == "__main__":
    # This block will not be executed when imported
    pass 