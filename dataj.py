import sqlite3

obj = []
alarm_obj=[]


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
    ##print("came here add")
    #c.execute("select time_stamp from reminder_db")

    ##print([int(record[0]) for record in c.fetchall()])
    ##print ("pre")
    del obj[:]
    con.commit()



def delete_reminder(id):
    con = sqlite3.connect("test.db")
    c = con.cursor()
    ##print (id)
    c.execute('DELETE FROM reminder_db WHERE _id=?', (id,))

    con.commit()
    ##print("came here delete")

def add_alarm(time,des,tunnel,repeat,g):
    nc = sqlite3.connect("alarm.db")
    alarm_obj.append((time,des,tunnel,repeat,g))
    ncursor = nc.cursor()
    #print ('jerey too')
    ncursor.executemany('INSERT INTO alarm_db(time_stamp,des,tunnel,repeat,guild) VALUES (?,?,?,?,?)',alarm_obj)


    ncursor.execute("select _id from alarm_db")
    del alarm_obj[:]
    #print([int(record[0]) for record in ncursor.fetchall()])
    #print ("pre")
    nc.commit()

def delete_repeat_alarm(id,xx):
    ncv = sqlite3.connect("alarm.db")
    ncursor = ncv.cursor()

    for drow in ncursor.execute("SELECT _id, time_stamp, des, tunnel ,repeat,guild from alarm_db"):
        #print(str(xx)+'\n'+ str(int(drow[5]))+ '\n' + str(id) + '\n' + str(int(drow[0])))
        if xx == int(drow[5]) and id == drow[0]:
            ncursor.execute("DELETE FROM alarm_db WHERE _id = ?", (id,))
            ncv.commit()
            return 'Delete Succesful'


    return 'Unsuccessful check ID carefully by $list_alarm'




def return_l(xx):
    new_con = sqlite3.connect('alarm.db')
    msg = ''
    id = []
    nc = new_con.cursor()

    for drow in nc.execute("SELECT _id, time_stamp, des, tunnel ,repeat,guild from alarm_db"):
        #print(drow[5])
        if (xx == int(drow[5])):
            id.append(drow[0])
            msg = msg + 'ALARM ID:{} |Time: {} |Name: {} |Repeat: {}\n'.format(drow[0], drow[1], drow[2], drow[4])
    return(msg)