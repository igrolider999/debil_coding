#pidoras
import sqlite3

connection = sqlite3.connect('gym_stats.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS progress(hp INTEGER, bucks INTEGER, damage INTEGER)""")


# cursor.execute("INSERT INTO progress VALUES (90, 1400, 10)")

cursor.execute("SELECT * FROM progress")

result = cursor.fetchall()
print(result)

cursor.execute("""DELETE FROM progress WHERE hp = 90""")

connection.commit()
connection.close()