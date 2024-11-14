# performance_tracking.py

import time

class PerformanceTracking:
    def __init__(self):
        self.tasks = []

    def start_task(self, task_name):
        task_data = {
            "name": task_name,
            "start_time": time.time(),
            "completed": False,
            "accuracy": None
        }
        self.tasks.append(task_data)
        print(f"Task '{task_name}' started.")

    def complete_task(self, task_name, accuracy_score):
        task = next((t for t in self.tasks if t["name"] == task_name and not t["completed"]), None)
        if task:
            task["end_time"] = time.time()
            task["completed"] = True
            task["accuracy"] = accuracy_score
            task["duration"] = task["end_time"] - task["start_time"]
            print(f"Task '{task_name}' completed with accuracy {accuracy_score}. Duration: {task['duration']} seconds.")

    def get_performance_report(self):
        return self.tasks

# Usage example
performance = PerformanceTracking()
performance.start_task("Math Problem #1")
time.sleep(3)  # Simulate time taken to complete the task
performance.complete_task("Math Problem #1", accuracy_score=0.85)
print("Performance Report:", performance.get_performance_report())

