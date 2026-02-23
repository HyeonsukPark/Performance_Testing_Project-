# Performance Testing Project – Flask + Locust (Windows)

## 1. Project Objective

This project demonstrates performance testing of a Python-based web application using Locust. The goal of this project is to simulate and analyze system performance under concurrent user load.

The goals of this project are:

- Simulate concurrent user load
- Compare CPU-bound and I/O-bound behavior
- Measure latency, throughput, and failure rate
- Observe system resource usage (CPU and memory)
- Identify bottlenecks
- Evaluate performance improvements
  

## 2. Environment

Windows, Python, Flask, Locust


## 3. Flask Application Design

The Flask app includes three endpoints:

### `/health`
Lightweight endpoint for baseline latency measurement.

### `/io`
Simulates I/O-bound behavior using `time.sleep()`.

### `/cpu`
Simulates CPU-bound workload via heavy computation loop.

## 4. Running the Application

### Step 1: Install dependencies

```
pip install -r requirements.txt
```

### Step 2: Start Flask server

```
python app/app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

## 5. Running Load Tests

### Step 1: Start Locust

```
locust -f locustfile.py
```

### Step 2: Open Locust UI

Open browser:

```
http://localhost:8089
```

Recommended test plan:

| Users | Ramp up | Duration |
|--------|------------|----------|
| 10 | 2 | 3 min |
| 50 | 5 | 3 min |
| 100 | 10 | 3 min |

Number of users = total concurrent users

Ramp up (users started/second) = spawn rate


## 7. Metrics Collected

From Locust:

- Average Response Time
- 95th Percentile (P95)
- Requests per Second (RPS)
- Failure Rate

From Windows Task Manager:

- CPU Utilization
- Memory Usage

Optional logging:

```
python monitor.py
```

This logs CPU and memory usage to CSV.


## 8. Observations Template

### 10 Users

- Average Response Time: 74.66 ms
- P95 Response Time: 220 ms 
- Requests per Second (RPS): 25.9
- Failures: 0
- CPU: 54.4%
- Memory: 8.3%

Observation:

Under mixed workload (10 users, ramp-up 2/sec, 180s duration), the aggregated average latency was 74.66 ms with no failures. However, endpoint-level analysis revealed that the /io endpoint exhibited significantly higher latency (Avg 211 ms, P95 230 ms), indicating I/O-bound behavior dominating tail latency.

---

### 50 Users

- Average Response Time: 102.73 ms
- P95 Response Time: 280 ms 
- Requests per Second (RPS): 122.6
- Failures: 0
- CPU: 54.4%
- Memory: 13%

Observation:

At 50 concurrent users, the system demonstrated near-linear throughput scaling (122 RPS vs 26 RPS at 10 users). While average latency increased moderately (102 ms), no failures were observed. The /io endpoint continued to dominate tail latency, suggesting I/O-bound behavior as the primary contributor to P95 degradation under load.

---

### 100 Users

- Average Response Time: 256.23 ms
- P95 Response Time: 610 ms 
- Requests per Second (RPS): 122
- Failures: 7046
- CPU: 54.4%
- Memory: 18%

Observation:

At 100 concurrent users, throughput plateaued at ~122 RPS, identical to the 50-user scenario. However, latency increased significantly (P95 610 ms) and failures appeared (7046 total). This indicates that the system reached its maximum processing capacity, resulting in request queuing and saturation behavior.



## 10. Failure Analysis 

Error message: OSError(10048, '[WinError 10048] Only one usage of each socket address (protocol/network address/port) is normally permitted.')

The message indicates that Windows ran out of available ephemeral TCP ports. The errors were caused by Windows networking limits. 


## 11. Conclusions

This project demonstrates:

- Differences between CPU-bound and I/O-bound bottlenecks
- Impact of concurrency on latency distribution
- Importance of system resource monitoring
- Effect of server configuration on performance



