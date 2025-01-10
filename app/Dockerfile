ARG version=3.12-alpine
FROM python:$version
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ARG PYTHONENV=/app
ENTRYPOINT ["python"]
CMD ["/app/main.py"]
