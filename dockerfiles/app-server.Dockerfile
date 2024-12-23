ARG version=3.12-slim
FROM python:$version
WORKDIR /app
COPY ../requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY ../server /app/server
COPY ../.env /app
ENV PYTHONPATH=/app
ENTRYPOINT ["python"]
CMD ["/app/server/main/app.py"]