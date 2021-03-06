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

    sql1 = ("SELECT team_id, team_name, mascot FROM team")
    sql2 = ("SELECT player_id, first_name, last_name, team_id FROM player")

    cursor.execute(sql1)

    teams = cursor.fetchall()

    print("--DISPLAYING TEAM RECORDS--")

    for team_id, team_name, mascot in teams:
        print("Team ID: {}".format(team_id))
        print("Team Name: {}".format(team_name))
        print("Mascot: {}".format(mascot))

    cursor.execute(sql2)
    players = cursor.fetchall()
    print()

    print("--DISPLAYING PLAYER RECORDS--")

    for player_id, first_name, last_name, team_id in players:
        print("Player ID: {}".format(player_id))
        print("First Name: {}".format(first_name))
        print("Last Name: {}".format(last_name))
        print("Team ID: {}".format(team_id))

    
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACESS_DENIED_ERROR:
        print(" The supplied user name or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()



