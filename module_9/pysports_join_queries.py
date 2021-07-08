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

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
    players = cursor.fetchall()
    print()

    print("--DISPLAYING PLAYER RECORDS--")

    for player_id, first_name, last_name, team_name in players:
        print("Player ID: {}".format(player_id))
        print("First Name: {}".format(first_name))
        print("Last Name: {}".format(last_name))
        print("Team Name: {}".format(team_name))
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
        
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


