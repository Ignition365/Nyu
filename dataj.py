import sqlite3

obj = []


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def add_reminder(req, des,tunnel):
    con = sqlite3.connect("test.db")
    obj.append((req, des,tunnel))
    c = con.cursor()
    c.executemany('INSERT INTO reminder_db(time_stamp,des,tunnel) VALUES (?,?,?)', obj)
    #print("came here add")
    c.execute("select time_stamp from reminder_db")

    #print([int(record[0]) for record in c.fetchall()])
    #print ("pre")
    del obj[:]
    con.commit()



def delete_reminder(id):
    con = sqlite3.connect("test.db")
    c = con.cursor()
    #print (id)
    c.execute('DELETE FROM reminder_db WHERE _id=?', (id,))
    con.commit()
    #print("came here delete")
