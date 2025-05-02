def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    
    Args:
        mongo_collection: pymongo collection object
        
    Returns:
        A list of all documents in the collection, or an empty list if no documents exist.
    """
    documents = list(mongo_collection.find())
    return documents if documents else []