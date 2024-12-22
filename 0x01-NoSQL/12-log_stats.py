#!/usr/bin/env python3

"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nginx = client.logs.nginx

method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print("{} logs".format(len(list(nginx.find()))))

for mthd in method:
    print("\tmethod {}: {}"
          .format(mthd, len(list(nginx.find({"method": mthd})))))

print("{} status check"
      .format(len(list(nginx.find({"method": "GET", "path": "/status"})))))
