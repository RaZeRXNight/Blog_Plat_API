from os import path, getenv
from dotenv import load_dotenv
from flask import Flask, Blueprint, request, jsonify
from json import loads, dumps
import sqlite3

# Load the Environment Variables.
if not path.isfile(".env") and not load_dotenv(".env"):
    raise Exception("ERROR: .Env File failed to load.")

def main():
    APP_NAME = getenv("APP_NAME")
    app = Flask(__name__)
    DB_CONN = "app/Blog.db"
    
    sql_con = sqlite3.connect(DB_CONN)
    cursor = sql_con.cursor()

    # Creates the blog post table if it doesn't exist.
    if not sql_con.execute("Select name from sqlite_master where type='table'").fetchall():
        sql_con.execute("""
                        create table pages(
                            id integer primary key, 
                            title varchar(200) not null, 
                            content varchar(1000) not null, 
                            category varchar(20) not null, 
                            tags varchar(50) null)
                            """
                        )

    @app.route("/")
    def home():
        return "WELCOME HOME"
    
    # Routes
    @app.get("/posts")
    def list_posts():
        sql_con = sqlite3.connect(DB_CONN).cursor()
        
        json = {
            "Results": sql_con.execute("select * from pages").fetchall()
        }
        return jsonify(json), 200

    @app.post("/posts")
    def blog_post():
        sql_con = sqlite3.connect(DB_CONN)
        cursor = sql_con.cursor()
        
        content = request.get_data().decode()
        json = loads(content)
        
        query = "insert into pages(title, content, category, tags) Values (?, ?, ?, ?);"
        data = (json["title"], json["content"], json["category"], dumps(json["tags"]))
        result = cursor.execute(query, data)
        
        if result:
            sql_con.commit()
            return {"content": "Success!"}
        return ""

    @app.route("/posts/<post_id>", methods=["POST", "GET", "PUT", "DELETE"])
    def post_operations(post_id):
        sql_con = sqlite3.connect(DB_CONN)
        # Check for ID Validity 
        try:
            if request.method == "GET":
                query = f"select * from pages where id='{post_id}'"
                cursor = sql_con.cursor()
                
                return jsonify({"Result": cursor.execute(query).fetchone()})
            if request.method == "PUT":
                data = loads(request.get_data().decode())
                query = f"""update pages
                set title = '{data["title"]}', content = '{data["content"]}', category = '{data["category"]}', tags = '{dumps(data["tags"])}'
                where id='{post_id}';
                """
                
                json = (data["title"], data["content"], data["category"], dumps(data["tags"]))
                
                cursor = sql_con.cursor()
                sql_con.commit()
                
                return jsonify({"Result": "SUCCESS!"})
            if request.method == "DELETE":
                query = f"delete from pages where id='{post_id}'"
                cursor = sql_con.cursor()
                cursor.execute(query)
                sql_con.commit()
                return jsonify({"Result": "Success!"})
            
        except Exception as e:
            return e
    app.run(host=getenv("HOST"), port=getenv("PORT"), debug=True)

if __name__ == "__main__":
    main()