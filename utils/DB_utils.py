import sqlite3


class Database(object):

    """
    Creating a sqlite3 database for storing players, counting games and wins
    """


    def __init__(self):

        self.conn = sqlite3.connect("munchkinPlayers.db")

        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, "
                         "name text, "
                         "gender text, "
                         "gamesplayed integer, "
                         "wins integer)"
                         )

        self.conn.commit()


    def addPlayer(self, name, gender, gamesplayed, wins):

        self.cur.execute("INSERT INTO players VALUES (NULL, ?, ?, ?, ?)", (name, gender, gamesplayed, wins, ))

        self.conn.commit()
        print("Player added")

        print(self.view())

    def view(self):

        self.cur.execute("SELECT * FROM players")

        rows = self.cur.fetchall()

        return rows

    def update(self, id, name, gamesplayed, wins):

        self.cur.execute("UPDATE players SET name=?, gamesplayed=?, wins=? WHERE id=?", (name, gamesplayed, wins, id))

        self.conn.commit()

    def search(self, name="", gamesplayed="", wins=""):
        self.cur.execute("SELECT * FROM players WHERE name=? OR gamesplayed=? OR wins=?",
                         (name, gamesplayed, wins))
        rows = self.cur.fetchall()
        return rows

    def removePlayer(self, name, rounds, wins):

        self.cur.execute("DELETE FROM players WHERE name=? AND gamesplayed=? AND wins=?", (name, rounds, wins,))

        self.conn.commit()

    def getPlayerByName(self, name):

        self.cur.execute("SELECT * FROM players WHERE name=?", (name,))

        rows = self.cur.fetchall()

        return rows

    def getPlayerId(self, name, rounds, wins):

        self.cur.execute("SELECT id FROM players WHERE name=? AND gamesplayed=? AND wins=?", (name, rounds, wins,))

        rows = self.cur.fetchall()

        return rows

    def getPlayerNames(self):

        self.cur.execute("SELECT name FROM players")

        names = self.cur.fetchall()

        return names

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':

    dbo = Database()
    #
    # dbo.addPlayer("Szandi", "female", 9, 3)
    # dbo.addPlayer("Bence", "male", 9, 2)
    # dbo.addPlayer("Máté", "male", 9, 2)
    # dbo.addPlayer("Gergely", "male", 9, 2)
    dbo.addPlayer("Tomi", "neutral", 1, 1)

    players = dbo.getPlayerByName("Máté")

    print(players)
