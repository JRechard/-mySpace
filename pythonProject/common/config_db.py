import pymongo


class ConfigMongodb:
    def __init__(self, host, port, username, password, db_name):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name

    def connect_db(self):
        conn = pymongo.MongoClient(
            host=self.host,
            port=self.port
        )
        database = conn[self.db_name]
        database.authenticate(name=self.username, password=self.password)
        return database


client = ConfigMongodb("123.206.217.183", 27017, "milu", "KuJ9i_of3hU_dGz3d", "mintmuse")
db = client.connect_db()
for i in db.list_collection_names():
    print(i)
