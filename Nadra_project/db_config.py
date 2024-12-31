import oracledb as cx_Oracle

def get_connection():
    cx_Oracle.init_oracle_client(lib_dir=r'C:\oraclexe\instantclient_23_6')
    username = 'HR'
    password = 'vinodvk'
    dsn = 'localhost/xe'

    conn = cx_Oracle.connect(
        user=username,
        password=password,
        dsn=dsn
    )
    return conn