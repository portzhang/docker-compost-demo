from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# 从环境变量获取数据库配置（由Compose传递）
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# 连接数据库并创建测试表
def init_db():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20))")
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def hello():
    init_db()
    return "Flask + MySQL 应用启动成功！"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)