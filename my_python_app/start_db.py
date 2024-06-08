from connect_DB import connect_CH

def create_test_db():
    client = connect_CH()

    client.execute("""
        create database if not exists docker
        """)
    
    client.execute("""
        create table if not exists docker.my_app
                   (
                        number UInt16
                        , dt_load DateTime materialized now()
                   )
        engine MergeTree
        order by dt_load
        """)
    
