import sqlite3
import os

DBCHECK = """
SELECT COUNT(name) FROM sqlite_master 
WHERE type='table' AND name='mibcache'
"""

DBINIT = """
CREATE TABLE mibcache (
    module TEXT NOT NULL,
    object TEXT NOT NULL,
    UNIQUE(module, object) ON CONFLICT REPLACE
)
"""

INSERT_MIB = "INSERT INTO mibcache (module, object) VALUES (?,?)"

SELECT_MIB = "SELECT module, object FROM mibcache where object=?"

class MibCache(object):
    def __init__(self, dbfile):
        self.db = sqlite3.connect(dbfile)
        dbcheck = self.db.execute(DBCHECK).fetchone()[0]
        if not dbcheck:
            self.db.execute(DBINIT)

    def saverows(self, source):
        for module, oid in source:
            self.db.execute(INSERT_MIB, [module, oid])
        self.db.commit()
            
    def checkmodule(self, oid):
        module = self.db.execute(SELECT_MIB, [oid]).fetchone()
        if module:
            return module[0]
        else:
            return None
