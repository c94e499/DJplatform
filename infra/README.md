# Mixcraft DJ Platform - Infrastructure

本目录包含 Mixcraft DJ 创作平台的基础设施配置。

## 目录结构

```
infra/
├── docker-compose.yml    # Docker Compose 配置
├── nginx/
│   └── nginx.conf        # Nginx 反向代理配置
├── .env.example          # 环境变量示例
└── README.md             # 本文件
```

## 快速开始

### 1. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 文件，修改必要的配置
```

### 2. 启动服务

```bash
docker-compose up -d
```

### 3. 访问应用

- 前端: http://localhost
- API: http://localhost/api

## 服务说明

| 服务 | 端口 | 说明 |
|------|------|------|
| nginx | 80 | 反向代理，统一入口 |
| frontend | - | Vue3 前端应用 |
| backend | 5000 | Flask API 后端 |
| db | 5432 | PostgreSQL 数据库 |

## 开发模式

如需单独运行服务进行开发：

### 后端

```bash
cd ../backend
pip install -r requirements.txt
python run.py
```

### 前端

```bash
cd ../frontend
npm install
npm run dev
```

## 注意事项

- 生产环境请务必修改 `.env` 中的密钥
- 数据库数据存储在 Docker volume 中
- 日志可通过 `docker-compose logs` 查看
