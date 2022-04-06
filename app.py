import os
import sqlite3
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

cur = sqlite3.connect('ticketsense.db')


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
        print(newlink[0])
        print(newfilmname[0])
        print(startdate)
        print(enddate)
        print((link.rsplit('/'))[2])

        db = cur.cursor()
        db.execute("INSERT INTO ticketsensedata (link, name, startday, endday) VALUES (?, ?, ?, ?)", newlink[0], newfilmname[0], startdate[0], enddate[0])
        cur.commit()

        return redirect("/submitted")
    else:
        return render_template("index.html")


@app.route("/submitted")
def submitted():
    return render_template("submitted.html")