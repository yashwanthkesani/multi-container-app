from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Backend API working!")

@app.route('/db')
def db_check():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        database=os.getenv("DB_NAME", "appdb")
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    result = cur.fetchone()
    return jsonify(database_version=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
