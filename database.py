import sqlite3
CREATE_TEST_TABLE ="CREATE TABLE IF NOT EXISTS TEST(Name TEXT,Tema5 REAL,Tema10 REAL,Tema20 REAL,Time INTEGER,TimeFrame INTEGER);"
INSERT_TEST = "INSERT INTO TEST (Name,Tema5,Tema10,Tema20,Time,TimeFrame) VALUES (?,?,?,?,?,?);"
Get_ALL_TEST = "SELECT * FROM TEST;"
GET_TEST_BY_TIME = "SELECT * FROM TEST WHERE Time<=? ORDER BY Time DESC LIMIT 100;"
#GET_TEST_BY_TIME = "SELECT * FROM TEST WHERE Time BETWEEN ? AND ?;"
def connect():
    return sqlite3.connect('test.db')
def create_table(connection):
    with connection:
        connection.execute(CREATE_TEST_TABLE)
def add_test(connection,Name,Tema5,Tema10,Tema20,Time,TimeFrame):
    with connection:
        connection.execute(INSERT_TEST,(Name,Tema5,Tema10,Tema20,Time,TimeFrame))
def get_all_test(connection):
    with connection:
        return connection.execute(Get_ALL_TEST).fetchall()
def get_test_by_time(connection,Time_cur):
    with connection:
        return connection.execute(GET_TEST_BY_TIME,(Time_cur,)).fetchall()
