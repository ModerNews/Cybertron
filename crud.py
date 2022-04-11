from pymysql import Connection
from models import from_tuple, EpisodeModel
from typing import Optional


def get_episodes(con: Connection, title: Optional[str]) -> list[tuple]:
    with con.cursor() as cur:
        query = f'SELECT * FROM Episodes{f" WHERE serie_id = {title}" if title else ""}'
        print(query)
        cur.execute(query)
        return list(cur.fetchall())