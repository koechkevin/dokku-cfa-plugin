#!/usr/bin/env python3

from utils import pip_install

def drop_mongodb_database(url):
    print("deleting {url}")
    pip_install("pymongo")
    import pymongo
    try:
        # Parse the MongoDB URL
        parsed_url = urlparse(url)
        username = parsed_url.username
        password = parsed_url.password
        hostname = parsed_url.hostname
        port = parsed_url.port
        db_name = parsed_url.path.replace("/", "")
        client = pymongo.MongoClient(host=hostname, port=port,
                                     username=username, password=password)
        
        db = client[db_name]
        client.drop_database(db_name)
        
        print(f"Database '{db_name}' deleted successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")