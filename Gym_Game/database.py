#pidoras
import sqlite3

connection = sqlite3.connect('Gym_Game/gym_stats.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS progress(hp INTEGER, bucks INTEGER, damage INTEGER)""")


# cursor.execute("INSERT INTO progress VALUES (90, 1400, 10)")
a = input()
b = input()
c = input()
cursor.execute(f"INSERT INTO progress VALUES ({a}, {b}, {c})")

cursor.execute("SELECT bucks FROM progress WHERE hp = 15")

result = cursor.fetchall()
print(result[3])

# cursor.execute("""DELETE FROM progress""")

connection.commit()
connection.close()
