import os
from flask import Flask, redirect, render_template, request
import pyodbc
import time
import random
import redis
import pickle
import hashlib

application = app = Flask(_name_)
server = 'ameydhuri.database.windows.net'
database = 'adb'
username = 'ameydhuri'
password = 'Kavya@2309'
driver = '{ODBC Driver 17 for SQL Server}'
# myHostname = "amey.redis.cache.windows.net"
# myPassword = "gDnvwj+XPhMOz3QaFuD1+K4nARWp2CMhvqiWJurR7Mk="
#
# r = redis.Redis(host='amey.redis.cache.windows.net',
#                 port=6379, db=0, password='gDnvwj+XPhMOz3QaFuD1+K4nARWp2CMhvqiWJurR7Mk=')


def disdata():
    cnxn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    print("Hi")
    cursor = cnxn.cursor()
    start = time.time()
    cursor.execute("SELECT TOP 10000 * FROM [quake]")
    row = cursor.fetchall()
    end = time.time()
    executiontime = end - start
    return render_template('searchearth.html', ci=row, t=executiontime)


def randrange(rangfro=None, rangto=None, num=None):
    dbconn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = dbconn.cursor()
    start = time.time()
    timeq = []
    mag1_li = []
    mag2_li = []
    time_li = []
    final = []
    for i in range(0, int(num)):
        mag1 = round(random.uniform(rangfro, rangto), 1)
        mag2 = round(random.uniform(rangfro, rangto), 1)
        if mag1 > mag2:
            success = "SELECT count(*) from [quake] where depth>'" + str(mag2) + "' and depth <" + str(mag1)
        else:
            success = "SELECT count(*) from [quake] where depth>'" + str(mag1) + "' and depth <" + str(mag2)

        print(mag1)
        print(mag2)
        hash = hashlib.sha224(success.encode('utf-8')).hexdigest()
        key = "redis_cache:" + hash

        if (r.get(key)):
            print("redis cached")
        else:
            print(key)
            print(r)
            # Do MySQL query
            print("Execution failed")
            cursor.execute(success)
            data = cursor.fetchall()
            rows = []
            for j in data:
                print(j)
                row_count = j
                rows.append(str(j))
                new_row = rows
            # Put data into cache for 1 hour
            r.set(key, pickle.dumps(list(rows)))
            r.expire(key, 36);

        # if (i < 1):
        first_time = time.time()
        first_execute = first_time - start
        timeq.append(first_execute)
        check123 = "The Depth 1 " + str(mag1) + " The Depth 2 " + str(mag2) + " The time is " + str(
            first_execute) + "The count is " + str(row_count)
        final.append(check123)
        print(first_execute)

        # print(new_row)
        # print ("Hello")

        cursor.execute(success)
    print("Step4")
    # print(rows)
    end = time.time()
    exectime = end - start
    return render_template('count.html', t=final, u=mag2_li, s=timeq, ci=rows, en=exectime)


def randrange_time(rangfro=None, rangto=None, num=None):
    dbconn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = dbconn.cursor()
    start = time.time()
    timeq = []
    mag1_li = []
    mag2_li = []
    time_li = []
    final = []
    for i in range(0, int(num)):
        mag1 = round(random.uniform(rangfro, rangto), 1)
        mag2 = round(random.uniform(rangfro, rangto), 1)
        if mag1 > mag2:
            success = "SELECT count(*) from [quake] where depth>'" + str(mag2) + "' and depth <" + str(mag1)
        else:
            success = "SELECT count(*) from [quake] where depth>'" + str(mag1) + "' and depth <" + str(mag2)
        # Do MySQL query
        print("Execution failed")
        cursor.execute(success)
        data = cursor.fetchall()
        rows = []
        row_count = 0
        for j in data:
            print(j)
            row_count = j
            rows.append(str(j))
            new_row = rows
        first_time = time.time()
        first_execute = first_time - start
        timeq.append(first_execute)
        check123 = "The Depth 1 " + str(mag1) + " The Depth 2 " + str(mag2) + " The time is " + str(
            first_execute) + "The count is " + str(row_count)
        final.append(check123)
        print(first_execute)

        # print(new_row)
        # print ("Hello")

        cursor.execute(success)
    print("Step4")
    # print(rows)
    end = time.time()
    exectime = end - start
    return render_template('count123.html', t=final, u=mag2_li, s=timeq, ci=rows, en=exectime)


def randrange_out(rangfro=None, rangto=None, num=None):
    dbconn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = dbconn.cursor()
    start = time.time()
    timeq = []
    mag1_li = []
    mag2_li = []
    time_li = []
    final = []
    for i in range(0, int(num)):
        mag1 = round(random.uniform(rangfro, rangto), 1)
        mag2 = round(random.uniform(rangfro, rangto), 1)
        if mag1 > mag2:
            success = "SELECT count(*) from [quake] where depth>'" + str(mag2) + "' and depth <" + str(mag1)
        else:
            success = "SELECT count(*) from [quake] where depth>'" + str(mag1) + "' and depth <" + str(mag2)

        print(mag1)
        print(mag2)
        hash = hashlib.sha224(success.encode('utf-8')).hexdigest()
        key = "redis_cache:" + hash

        if (r.get(key)):
            print("redis cached")
        else:
            print(key)
            print(r)
            # Do MySQL query
            print("Execution failed")
            cursor.execute(success)
            data = cursor.fetchall()
            rows = []
            row_count = 0
            for j in data:
                print(j)
                row_count = j
                rows.append(str(j))
                new_row = rows
            # Put data into cache for 1 hour
            r.set(key, pickle.dumps(list(rows)))
            r.expire(key, 36);

        # if (i < 1):
        first_time = time.time()
        first_execute = first_time - start
        timeq.append(first_execute)
        check123 = "The Depth 1 " + str(mag1) + " The Depth 2 " + str(mag2) + " The time is " + str(
            first_execute) + "The count is " + str(row_count)
        final.append(check123)
        print(first_execute)

        # print(new_row)
        # print ("Hello")

        cursor.execute(success)
    print("Step4")
    # print(rows)
    end = time.time()
    exectime = end - start
    return render_template('count1.html', t=final, u=mag2_li, s=timeq, ci=rows, en=exectime)


def randrange1(rangfro=None, rangto=None, lat1=None):
    dbconn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = dbconn.cursor()

    success = "SELECT latitude,longitude,time,depth from [quake] where depth>'" + str(
        rangfro) + "' and depth <'" + str(rangto) \
              + "' and latitude>" + str(lat1)

    print("Execution failed")
    cursor.execute(success)
    data = cursor.fetchall()
    print("Step4")
    print(data)
    return render_template('searchearth.html', ci=data)




def splitdatabar(year=None, split=None):
    dbconn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = dbconn.cursor()
    cursor = dbconn.cursor()
    pop1 = 0
    pop2 = 0
    ye = str(year)
    pop = int(20000000 / int(split - 1))
    print(pop)
    rows = []
    rows = list([['population', 'no of states']])
    arr = []
    while (pop1 <= 20000000):
        pop2 = pop1 + pop
        sql = "select '" + str(100000) + "',count(*) from year where \"" + str(year) + "\" between '" + str(
            pop1) + "' and '" + str(pop2) + "'"
        print(pop1)
        print(pop2)
        cursor.execute(sql)
        data = cursor.fetchall()
        for j in data:
            rows.append(list(j))
            print((rows))
        pop1 = pop2
    arr.append(rows)


    return render_template('resultsbar.html', data=rows, ci=arr)


def splitdatapie(split=None, year=None):
    dbconn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = dbconn.cursor()
    pop1 = 0
    pop2 = 0
    ye = str(year)
    pop = int(20000000 / int(split - 1))
    print(pop)
    rows = []
    rows = list([['population', 'no of states']])
    arr = []
    while (pop1 <= 20000000):
        pop2 = pop1 + pop
        sql="select '" + str(100000) + "',count(*) from year where \"" + str(year) +"\" between '" + str(pop1) + "' and '" + str(pop2) + "'"
        print(pop1)
        print(pop2)
        cursor.execute(sql)
        data = cursor.fetchall()
        for j in data:
            rows.append(list(j))
            print((rows))
        pop1 = pop2
    arr.append(rows)

    return render_template('resultspie.html', data=rows, ci=arr)








def splitdatasc(magone=None, magtwo=None, state=None):
    dbconn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = dbconn.cursor()
    ip1 = 0
    ip2 = 0
    ye = str(state)
    pop = float(30000000 / float(state))
    print(pop)
    rows = []
    rows = list([['population', 'Number of States']])
    arr = []
    while (ip1 < 30000000):
        ip2 = ip1 + pop
        sql = "select 1 ,count(*) from year where \"2015\"between " + str(ip1) + " and " + str(ip2)
        print(ip1)
        print(ip2)
        cursor.execute(sql)
        data = cursor.fetchall()
        for j in data:
            rows.append(list(j))

        ip1 = ip2 + pop
    arr.append(rows)
    print("Step4")
    print(arr)
    return render_template('resultssc.html', data=rows, ci=arr)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/displaydata', methods=['POST'])
def display():
    return disdata()


@app.route('/multiplerun', methods=['GET'])  # Redis cache extract
def randquery():
    rangfro = float(request.args.get('rangefrom'))
    rangto = float(request.args.get('rangeto'))
    num = request.args.get('nom')
    return randrange(rangfro, rangto, num)


@app.route('/multiplerun567', methods=['GET'])  # time
def randquery_out():
    rangfro = float(request.args.get('rangfro'))
    rangto = float(request.args.get('rangto'))
    num = request.args.get('nom')
    return randrange_out(rangfro, rangto, num)


@app.route('/multiplerun123', methods=['GET'])  # without redis/memcache extract
def randquery123():
    rangfro = float(request.args.get('rangefrom'))
    rangto = float(request.args.get('rangeto'))
    num = request.args.get('nom')
    return randrange_time(rangfro, rangto, num)


@app.route('/splitbar', methods=['GET'])  # split mag data
def magquery():
    split = int(request.args.get('split'))
    year = int(request.args.get('year'))
    return splitdatabar(year, split)


@app.route('/splitpie', methods=['GET'])  # split pie data
def magquerypie():
    #pop1 = float(request.args.get('pop1'))
    #pop2 = float(request.args.get('pop1'))
    split = int(request.args.get('split'))
    year = int(request.args.get('year'))

    return splitdatapie(split,year)


@app.route('/splitsc', methods=['GET'])  # scatter mag data
def magquerysc():
    mag1 = float(request.args.get('year1'))
    mag2 = float(request.args.get('year2'))
    state = request.args.get('state')
    return splitdatasc(mag1, mag2, state)


@app.route('/routeone', methods=['GET'])
def routeone():
    rangfro = float(request.args.get('rangefrom'))
    rangto = float(request.args.get('rangeto'))
    num = request.args.get('nom')
    print("in button")
    val = request.args.get('radio')
    print(val)
    if val == '0':  # without cache
        print("do something")
        return randrange_time(rangfro, rangto, num)
    elif val == '1':
        print("Do else")
        return randrange(rangfro, rangto, num)


# 5.59
if _name_ == '_main_':
    app.run()