FROM python:3.8-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]