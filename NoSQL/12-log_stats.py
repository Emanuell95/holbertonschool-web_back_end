#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def print_nginx_logs_stats():
    """
    Connect to MongoDB and print Nginx logs statistics
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the logs database and nginx collection
    logs_collection = client.logs.nginx
    
    # Get total number of logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Count methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")
    
    # Count status checks (GET /status)
    status_checks = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_checks} status check")


if __name__ == "__main__":
    print_nginx_logs_stats()
    