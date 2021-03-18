import pymongo

host = ""
port = 27017


class ConfigMongodb:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # self.admin = admin
        # self.password = password

    def connect_db(self):
        connection = pymongo.MongoClient(host=self.host, port=self.port)
        return connection


client = ConfigMongodb(host, port)
connection = client.connect_db()
