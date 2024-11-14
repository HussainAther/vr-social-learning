import time
from random import randint

# Simulated engagement metrics for each user
engagement_data = {user.name: {"interactions": 0, "tasks_completed": 0} for user in group.users}

# Function to simulate engagement tracking
def track_engagement(user):
    engagement_data[user.name]["interactions"] += randint(1, 5)  # Randomized for example
    engagement_data[user.name]["tasks_completed"] += randint(0, 2)

# Display engagement metrics in real-time
def display_engagement_metrics():
    while True:
        print("Real-Time Engagement Metrics:")
        for user, metrics in engagement_data.items():
            print(f"{user} - Interactions: {metrics['interactions']}, Tasks Completed: {metrics['tasks_completed']}")
        time.sleep(5)  # Update every 5 seconds

# Simulate engagement tracking for users
for user in group.users:
    track_engagement(user)

# Start displaying engagement metrics
display_engagement_metrics()

