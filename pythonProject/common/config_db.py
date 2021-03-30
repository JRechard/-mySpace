import pymongo


class ConfigMongodb:
    """
        配置数据库
    """
    def __init__(self, host, username, password, db_name, port=27017):
        self.host = host  # mongodb数据库的ip地址
        self.port = port  # mongodb数据库的默认端口号
        self.username = username  # 账户名
        self.password = password  # 密码
        self.db_name = db_name  # 被连接的数据库名

    # 连接数据库
    def connect_db(self):
        # 创建数据库连接对象
        conn = pymongo.MongoClient(
            host=self.host,
            port=self.port
        )
        database = conn[self.db_name]  # 连接数据库
        database.authenticate(name=self.username, password=self.password)  # 验证账户名与密码
        return database

    # 查询方法,返回布尔值
    def search_to_boolean(self, collection_name, data):
        db = self.connect_db()
        collection = db.get_collection(collection_name)
        cursor = collection.find(data)
        if list(cursor):
            return True
        else:
            return False

    # 查询方法
    def search(self, collection_name, data):
        db = self.connect_db()
        collection = db.get_collection(collection_name)
        cursor = collection.find(data)
        return list(cursor)
