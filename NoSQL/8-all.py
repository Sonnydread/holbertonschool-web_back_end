#!/usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    document_list = [doc for doc in mongo_collection.find()]
    return document_list
