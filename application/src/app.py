from flask import Flask, jsonify, request
from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST
)
import time

app = Flask(__name__)

orders = []

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total de requisicoes HTTP",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Tempo de resposta das requisicoes"
)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_metrics(response):
    duration = time.time() - request.start_time

    REQUEST_COUNT.labels(
        request.method,
        request.endpoint or "unknown",
        response.status_code
    ).inc()

    REQUEST_LATENCY.observe(duration)

    return response

@app.route("/")
def home():
    return jsonify({
        "application": "TechCorp Orders API",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json(silent=True) or {}

    if not data.get("product"):
        return jsonify({
            "error": "Product is required"
        }), 400

    order = {
        "id": len(orders) + 1,
        "product": data["product"],
        "status": "created"
    }

    orders.append(order)

    return jsonify(order), 201

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)