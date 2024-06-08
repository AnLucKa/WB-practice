import time
from clickhouse_driver import Client
import os


def get_param_connect() -> dict:
    param_connect = {}
    param_connect['host'] = os.getenv('CH_HOST') # 'localhost' 
    param_connect['user'] = os.getenv('CH_USER') # 'default'
    param_connect['password'] = os.getenv('CH_PASSWORD') # '' 
    param_connect['port'] = os.getenv('CH_PORT') # 9000

    return param_connect



def connect_CH() -> Client:

    param_connect = get_param_connect()

    for _ in range(7):
        try:
            client = Client(param_connect['host'],
                            user=param_connect['user'],
                            password=param_connect['password'],
                            port=param_connect['port'],
                            database='')
            
            return client
        except Exception as e:
            print(e, "Нет коннекта к КликХаус")
            time.sleep(60)