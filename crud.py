from pymysql import Connection
from models import *
from typing import Optional


def get_episodes(con: Connection, title: Optional[str]) -> list[tuple]:
    with con.cursor() as cur:
        apostrophe = "'"
        query = f'SELECT * FROM Translations.Episodes{f" WHERE serie_id = {apostrophe}{title}{apostrophe}" if title else ""}'
        print(query)
        cur.execute(query)
        return list(cur.fetchall())


def get_user_by_name(con: Connection, name: str):
    with con.cursor() as cur:
        cur.execute("SELECT * FROM test.users WHERE name = %s", (name,))
        return from_tuple(UserModel, cur.fetchone())