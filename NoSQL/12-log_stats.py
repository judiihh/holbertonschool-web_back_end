#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


if __name__ == "__main__":
    """Main execution block to connect to MongoDB and print stats."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total logs count
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check count
    status_check_count = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check") 