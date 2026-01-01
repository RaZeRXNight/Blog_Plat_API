from os import path, getenv
from dotenv import load_dotenv
from flask import Flask, Blueprint

import sqlite3

# Load the Environment Variables.
if not path.isfile(".env") and not load_dotenv(".env"):
    raise Exception("ERROR: .Env File failed to load.")

APP_NAME = getenv("APP_NAME")
app = Flask(__name__)
sql_con = sqlite3.connect("Blog.db")
cursor = sql_con.cursor()

print(sql_con.execute("Select name from sqlite_master where type='table'").fetchall())

# Creates the blog post table if it doesn't exist.
if not sql_con.execute("Select name from sqlite_master where type='table'").fetchall():
    sql_con.execute("create table pages(title, author, year)")

@app.route("/")
def home():
    return "WELCOME HOME"


def main():
    print("Hello from blog-api!")

if __name__ == "__main__":
    app.run(host=getenv("HOST"), port=getenv("PORT"), debug=True)
