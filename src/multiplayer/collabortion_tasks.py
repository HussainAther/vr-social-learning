# collaboration_tasks.py

class CollaborationTasks:
    def __init__(self):
        self.tasks = {}

    def create_task(self, task_name, assigned_group):
        self.tasks[task_name] = {
            "assigned_group": assigned_group,
            "status": "Incomplete",
            "contributors": []
        }
        print(f"Task '{task_name}' created for group '{assigned_group}'.")

    def update_task_status(self, task_name, status):
        if task_name in self.tasks:
            self.tasks[task_name]["status"] = status
            print(f"Task '{task_name}' status updated to {status}.")
        else:
            print(f"Task '{task_name}' not found.")

    def log_contribution(self, task_name, user):
        if task_name in self.tasks:
            self.tasks[task_name]["contributors"].append(user)
            print(f"User '{user}' contributed to task '{task_name}'.")

    def get_task_info(self, task_name):
        return self.tasks.get(task_name, "Task not found.")

# Usage example
tasks = CollaborationTasks()
tasks.create_task("Physics Experiment", "Study Group A")
tasks.log_contribution("Physics Experiment", "Alice")
tasks.update_task_status("Physics Experiment", "Complete")
print("Task Info:", tasks.get_task_info("Physics Experiment"))

