import time
import random
from start_db import create_test_db
from connect_DB import connect_CH



def start_simulation():
    client = connect_CH()

    while True:
        number = random.randint(1, 100000000)

        client.execute(f"""
            INSERT INTO docker.my_app
            select {number} number 
            """)

        qty_row = client.execute(f"""
            select count() from docker.my_app
            """)
        
        print('Добавлено строк - ', qty_row[0][0])

        time.sleep(1)

if __name__ == '__main__':
    create_test_db()
    start_simulation()
