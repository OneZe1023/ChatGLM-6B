# 使用官方的 Python 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制项目的 requirements.txt 文件到容器中
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt


# 复制整个项目到容器中
COPY . .

# 暴露应用程序运行的端口（根据需要修改）
EXPOSE 6666
EXPOSE 6667
EXPOSE 6668
EXPOSE 6669

# 设置容器启动时执行的命令
CMD ["python", "api.py"]
