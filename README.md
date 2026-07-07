# Flask + MySQL Docker 示例项目

一个使用 Docker Compose 快速搭建 Flask Web 应用与 MySQL 数据库的入门示例。

## 项目结构

```
docker-test/
├── app.py              # Flask 应用主文件
├── Dockerfile          # 构建 Flask 镜像的配置
├── docker-compose.yml  # Compose 编排文件（定义 web + mysql 两个服务）
├── requirements.txt    # Python 依赖清单
└── README.md           # 说明文件
```

## 技术栈

- **Web**: Flask 2.3.3
- **数据库**: MySQL 8.0
- **Python**: 3.9-slim
- **容器编排**: Docker Compose 3.8

## 快速启动

确保已安装 [Docker](https://www.docker.com/) 和 Docker Compose，然后在项目根目录执行：

```bash
docker-compose up -d
```

启动后访问 http://localhost:5000 ，页面应显示：

> Flask + MySQL 应用启动成功！

## 停止服务

```bash
docker-compose down
```

如需同时清除 MySQL 数据卷：

```bash
docker-compose down -v
```

## 配置说明

| 环境变量 | 值 | 说明 |
|---------|------|------|
| `DB_HOST` | mysql | Compose 内部服务名，自动网络解析 |
| `DB_USER` | root | MySQL 用户名 |
| `DB_PASSWORD` | 123456 | MySQL root 密码 |
| `DB_NAME` | flask_db | 自动创建的数据库 |

MySQL 数据通过命名卷 `mysql_data` 持久化存储，容器删除后数据不会丢失。

## 应用行为

Flask 应用启动后，每次访问根路由 `/` 时会自动连接 MySQL 并创建一张 `test` 表（如不存在）：

```sql
CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20))
```

## 开发模式

项目配置了代码卷挂载（`./:/app`），修改本地 `app.py` 后重启容器即可生效：

```bash
docker-compose restart web
```

无需重新构建镜像。
