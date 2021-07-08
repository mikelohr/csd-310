import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "Colin",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
try: 
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Ty', 'Robinson', 1);")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")

    players = cursor.fetchall()
    print()

    print("--DISPLAYING PLAYERS AFTER INSERT--")

    for player_id, first_name, last_name, team_name in players:
        print("Player ID: {}".format(player_id))
        print("First Name: {}".format(first_name))
        print("Last Name: {}".format(last_name))
        print("Team Name: {}".format(team_name))

    cursor.execute("UPDATE player SET team_id = 2 WHERE first_name = 'Ty';")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")

    players = cursor.fetchall()
    print()

    print("--DISPLAYING PLAYERS AFTER UPDATE--")

    for player_id, first_name, last_name, team_name in players:
        print("Player ID: {}".format(player_id))
        print("First Name: {}".format(first_name))
        print("Last Name: {}".format(last_name))
        print("Team Name: {}".format(team_name))

    
    cursor.execute("DELETE FROM player WHERE first_name = 'Ty';")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")

    players = cursor.fetchall()
    print()

    print("--DISPLAYING PLAYERS AFTER DELETE--")

    for player_id, first_name, last_name, team_name in players:
        print("Player ID: {}".format(player_id))
        print("First Name: {}".format(first_name))
        print("Last Name: {}".format(last_name))
        print("Team Name: {}".format(team_name))

        
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied user name or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()



