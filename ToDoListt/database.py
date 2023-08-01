import sqlite3

connection = sqlite3.connect('database.db')
my_cursor = connection.cursor()

def add(id, title, description, time, date):

    my_cursor.execute(f'INSERT INTO tasks(id, title, description, done, time, date, priority) VALUES({id} , "{title}", "{description}", 0 , "{time}", "{date}", 0)') # baray inke vasat string , variable bezarim aval string f mizarim
    connection.commit()


def getAll():
    my_cursor.execute('SELECT * FROM tasks')
    results = my_cursor.fetchall()
    return results


def updateDoneTasks(do, title):
    my_cursor.execute(f'UPDATE tasks SET done = {do} WHERE title = "{title}" ')
    connection.commit()

def deleteTasks(title):
    my_cursor.execute(f'DELETE FROM tasks WHERE title = "{title}"')
    connection.commit()

def priorityFunc(prio, title):
    my_cursor.execute(f'UPDATE tasks SET priority = {prio} WHERE title = "{title}" ')
    connection.commit()