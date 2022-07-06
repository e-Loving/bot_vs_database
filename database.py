import sqlite3

connection = sqlite3.connect("database.db", check_same_thread=False)
cursor = connection.cursor()


def add(name, user_id, word):
    if len(cursor.execute(f"SELECT * FROM sentences WHERE user_id = '{user_id}' AND word = '{word}'").fetchall()) == 0:
        cursor.execute("INSERT INTO sentences VALUES (?,?,?,?)", [name, user_id, word, 1])
    else:
        cursor.execute(f"UPDATE sentences SET count = count + 1 WHERE user_id = '{user_id}' AND word = '{word}'")
    connection.commit()


def fun():
    for name, word, count in [item for item in cursor.execute("SELECT name, word, count FROM sentences").fetchall()]:
        yield f"{name} {word} so'zini {count} marta ishlatdi"


def delete(who="any"):
    cursor.execute("DELETE FROM sentences") if who == "any" else cursor.execute(
        f"DELETE FROM sentences WHERE user_id = '{who}'")
    connection.commit()
