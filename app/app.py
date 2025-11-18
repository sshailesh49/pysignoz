    
from flask import Flask
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from opentelemetry import trace

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

@app.route("/")
def hello():
    return "Hello from ECS with OTEL!"

app.run(host="0.0.0.0", port=8080)
