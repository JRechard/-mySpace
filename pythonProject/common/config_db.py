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
