# engagement_metrics.py

import time
from random import randint

class EngagementMetrics:
    def __init__(self):
        self.metrics = {
            "active_time": 0,              # Time spent actively engaging
            "interactions": 0,             # Number of interactions (e.g., clicks, actions)
            "tasks_completed": 0           # Count of completed tasks
        }
        self.start_time = None

    def start_session(self):
        self.start_time = time.time()
        print("Engagement session started.")

    def stop_session(self):
        if self.start_time:
            self.metrics["active_time"] = time.time() - self.start_time
            self.start_time = None
            print("Engagement session ended.")
            print("Total active time:", self.metrics["active_time"])

    def log_interaction(self):
        self.metrics["interactions"] += 1
        print("Interaction logged. Total interactions:", self.metrics["interactions"])

    def complete_task(self):
        self.metrics["tasks_completed"] += 1
        print("Task completed. Total tasks completed:", self.metrics["tasks_completed"])

    def get_metrics(self):
        return self.metrics

# Usage example
engagement = EngagementMetrics()
engagement.start_session()
engagement.log_interaction()
engagement.complete_task()
time.sleep(2)  # Simulate active time
engagement.stop_session()
print("Engagement Metrics:", engagement.get_metrics())

