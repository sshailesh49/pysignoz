FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENV OTEL_SERVICE_NAME=ecs-python-app
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://172.83.83.98:4317
ENV OTEL_EXPORTER_OTLP_PROTOCOL=grpc
EXPOSE 8080
CMD ["python","app.py"]
