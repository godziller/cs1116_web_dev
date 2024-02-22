from flask import g 
import os 
import sqlite3

DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
        return g.db
    
def close_db(e=None):
    db = g.pop("db", None)
    if db  is not None:
        db.close()

class EurovisionDB:
    def __init__(self, name) -> None:
        DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
        if "db" not in g:
            g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
            g.db.row_factory = sqlite3.Row
        self.db_handle = g.db
        
    def getCountryCount(self, country):
        count = self.db_handle.execute("""SELECT COUNT (*) FROM winners WHERE country = ?; """, (country,)).fetchone()[0]
        print(type(count))
        print(count)
        return (count)

    def getSingersList(self,country):
        singers = self.db_handle.execute("""SELECT * FROM winners WHERE country = ?; """, (country,)).fetchall()
        print(type(singers))
        print(singers)
        return singers
    
    def getCountiesAbovePoints(self, points):
        countryList = self.db_handle.execute("""SELECT performer FROM winners WHERE points >= ?; """, (points,)).fetchall()
        return(countryList)
    
    def filterOnCountryAndPoints(self, country, points):
        singerList = self.db_handle.execute("""SELECT performer FROM winners WHERE country = ? AND points >= ?""", (country, points)).fetchall()
        return singerList
    
    def getAllWinners(self):
        singers = self.db_handle.execute("""SELECT performer FROM winners """, ).fetchall()
        return singers
