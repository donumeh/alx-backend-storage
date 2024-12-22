#!/usr/bin/env python3

"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def main():
    """
    main: print formatted details about nginx logs
    """

    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs".format(len(list(nginx.find()))))
    print("Methods:")

    for mthd in method:
        print("\tmethod {}: {}".format(mthd, len(list(nginx.find({"method": mthd})))))

    print(
        "{} status check".format(
            len(list(nginx.find({"method": "GET", "path": "/status"})))
        )
    )
    ips = top_ips(nginx)

    print("IPs:")

    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))


def top_ips(mongo_collection):
    """
    Gets all ips and their total number

    Args:
        mongo_collection: mong client

    Return: list of ip and their count
    """

    return list(
        mongo_collection.aggregate(
            [
                {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}},
                {"$limit": 10},
            ]
        )
    )


if __name__ == "__main__":
    main()
