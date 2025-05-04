#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Count of logs
    logs_count = logs_collection.count_documents({})
    print(f"{logs_count} logs")
    
    # Count of methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count of status checks
    status_check = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
    
    # Close the MongoDB connection
    client.close()
