import sqlite3
from langchain_community.utilities import SQLDatabase


class BaseDB:
    def __init__(self, db_url):
        self.conn = sqlite3.connect(db_url)

def SakilaDB(db_path=None, db_type=None):
    if not db_path:
        db_path = "/mnt/c/Users/conta/Downloads/Saklia/sqlite-sakila.db"
    if not db_type:
        db_type = "sqlite"

    db_uri = f"{db_type}:///{db_path}"
    db = SQLDatabase.from_uri(db_uri)
    return db