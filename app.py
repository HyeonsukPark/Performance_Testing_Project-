from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running"

@app.get("/health")
def health():
    return jsonify(status="ok")

# I/O-bound
@app.get("/io") 
def io_bound():
    time.sleep(0.2)
    return jsonify(result="slept")

# CPU-bound 
@app.get("/cpu") 
def cpu_bound():
    total = 0
    for i in range(500000):  
        total += i*i
    return jsonify(total=total)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

        