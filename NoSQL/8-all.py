#!/usr/bin/env python3
def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: A PyMongo collection object.

    Returns:
        A list of dictionaries, where each dictionary represents a document in the collection.
        Returns an empty list if the collection is empty.
    """
    documents = list(mongo_collection.find())
    return documents