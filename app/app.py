from flask import Flask
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
import time

app = Flask(__name__)

resource = Resource.create({"service.name": "ecs-python-app"})
trace_provider = TracerProvider(resource=resource)
otlp_exporter = OTLPSpanExporter(endpoint="http://172.83.83.98:4317")
trace_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))

from opentelemetry import trace
trace.set_tracer_provider(trace_provider)
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def index():
    return "Hello from ECS - SigNoz demo"

@app.route("/sleep")
def sleepy():
    time.sleep(0.5)
    return "slept 0.5s"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
