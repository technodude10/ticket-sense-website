import os
import sqlite3
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

      
def db_connection():
    db = sqlite3.connect('ticketsense.db')
    db.row_factory = sqlite3.Row
    return db


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("link")
        filmname = request.form.get("filmname")
        start = request.form.get("start")
        end = request.form.get("end")

        print(start)
        print(end)

        newlink = link.rsplit('/', 1)
        newfilmname = filmname.rsplit(' ', 1)
        startdate = start.rsplit('/')
        enddate = end.rsplit('/')
        print((link.rsplit('/'))[2])

        conn = db_connection()
        db = conn.cursor()
        db.execute("INSERT INTO ticketsensedata (link, name, startday, startmonth, startyear, endday, endmonth, endyear) VALUES (?, ?, ?, ?, ?, ? ,?, ?)", 
                  (newlink[0], newfilmname[0], startdate[0], startdate[1], startdate[2], enddate[0], enddate[1], enddate[2]))
        conn.commit()
        conn.close()

        db = db_connection()
        p = db.execute("SELECT * FROM ticketsensedata").fetchall()
        db.close()

        for i in p:
            print(i["name"])

        return redirect("/submitted")

        
    else:
        return render_template("index.html")


@app.route("/submitted")
def submitted():
    return render_template("submitted.html")