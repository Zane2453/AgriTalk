DEBUG = False

FLASK_SECRET_KEY = 'ZAQBsbWNxxyLHFBNQZugmPEd' # use random string, for example, "FGHJHGFDSDFGHGFDSWERE" 

# DB_CONFIG = '<database>[+<orm_lib>]://[<user>[:<password>]]<host>[:<port>]/[db_name][?charset=utf8]'
# ex: DB_CONFIG = 'mysql+pymysql://user:pass@localhost:3306/db_name?charset=utf8'
# ex: DB_CONFIG = 'sqlite+pysqlite:///db.sqlite3'
DB_CONFIG = 'mysql+pymysql://iottalk:pcs54784@localhost:3306/farm?charset=utf8'
DB_POOL_RECYCLE = 600
QUERY_LIMIT = 100
REQUEST_TIMEOUT = 10

CSM_HOST = 'farm.iottalk.tw'  # IoTtalk server's 'IP' or 'DomainName', for example, '8.8.8.8'
