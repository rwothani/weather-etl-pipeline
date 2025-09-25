FROM python:3.11-slim
WORKDIR /app
COPY scripts/hello.py .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "hello.py"]