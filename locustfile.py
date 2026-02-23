from locust import HttpUser, task, between 

class ApiUser(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(0.1, 0.5)
    
    @task(5)
    def health(self):
        self.client.get("/health")
        
    
    @task(3)
    def io(self):
        self.client.get("/io")
        
        
    @task(2)
    def cpu(self):
        self.client.get("/cpu")

