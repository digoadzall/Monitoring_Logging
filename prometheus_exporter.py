from prometheus_client import start_http_server, Summary, Counter
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

REQUEST_COUNT = Counter('model_requests_total', 'Total number of predictions')
REQUEST_LATENCY = Summary('model_request_latency_seconds', 'Latency of model prediction')

@app.route('/predict', methods=['POST'])
@REQUEST_LATENCY.time()
def predict():
    REQUEST_COUNT.inc()
    data = request.get_json()
    time.sleep(0.3)  # Simulasi prediksi
    prediction = {'result': 'churn'}  # Dummy
    return jsonify(prediction)

if __name__ == '__main__':
    start_http_server(8000)  # expose metrics here
    app.run(host='0.0.0.0', port=5000)