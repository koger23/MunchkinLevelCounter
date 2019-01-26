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
                         "wins integer,"
                         "roundsplayed integer)"
                         )

        self.conn.commit()


    def addPlayer(self, name, gender, gamesplayed, wins, roundsplayed=0):

        self.cur.execute("INSERT INTO players VALUES (NULL, ?, ?, ?, ?, ?)", (name, gender, gamesplayed, wins, roundsplayed,))

        self.conn.commit()

    def view(self):

        self.cur.execute("SELECT * FROM players")

        rows = self.cur.fetchall()

        return rows

    def updateAll(self, id, name="", gender="", gamesplayed="", wins="", roundsplayed=""):

        self.cur.execute("UPDATE players SET name=?, gender=?, gamesplayed=?, wins=?, roundsplayed=? WHERE id=?", (name, gender, gamesplayed, wins, roundsplayed, id,))

        self.conn.commit()

    def update(self, id, name="", gamesplayed="", wins="", roundsplayed=""):

        self.cur.execute("UPDATE players SET name=?, gamesplayed=?, wins=?, roundsplayed=? WHERE id=?", (name, gamesplayed, wins, roundsplayed, id,))

        self.conn.commit()

    def search(self, name="", gamesplayed="", wins="", id=""):
        self.cur.execute("SELECT * FROM players WHERE name=? OR gamesplayed=? OR wins=? OR id=?",
                         (name, gamesplayed, wins, id))
        rows = self.cur.fetchall()
        return rows

    def removePlayer(self, name, gamesplayed, wins):

        self.cur.execute("DELETE FROM players WHERE name=? AND gamesplayed=? AND wins=?", (name, gamesplayed, wins,))

        self.conn.commit()

    def getPlayerByName(self, name):

        self.cur.execute("SELECT * FROM players WHERE name=?", (name,))

        rows = self.cur.fetchall()

        return rows

    def getPlayerId(self, name, gamesplayed, wins):

        self.cur.execute("SELECT id FROM players WHERE name=? AND gamesplayed=? AND wins=?", (name, gamesplayed, wins,))

        rows = self.cur.fetchall()

        return rows

    def getPlayerNames(self):

        self.cur.execute("SELECT name FROM players")

        names = self.cur.fetchall()

        return names

    def getRounds(self, id):

        self.cur.execute("SELECT roundsplayed FROM players WHERE id=?", (id,))

        roundsPlayed = self.cur.fetchall()

        return roundsPlayed[0][0]

    def saveWins(self, id, wins):

        self.cur.execute("UPDATE players SET wins WHERE id=?", (id, wins,))

    def __del__(self):
        self.conn.close()

class SavedGameDB(object):

    def __init__(self):

        self.conn = sqlite3.connect("munchkinSavedGame.db")

        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, "
                         "datetime text, "
                         "gender text, "
                         "rounds integer, "
                         "player_ids text,"
                         "player_genders text)"
                         )

        self.conn.commit()


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
