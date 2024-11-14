# user_sync.py

import time

class UserSync:
    def __init__(self):
        self.user_positions = {}  # Dictionary to track user positions

    def update_position(self, user_id, position):
        # Update the position of a user
        self.user_positions[user_id] = position
        self.broadcast_position(user_id, position)

    def broadcast_position(self, user_id, position):
        # Broadcast position to other users (placeholder for actual networking code)
        print(f"User {user_id} is now at position {position}.")

    def get_user_position(self, user_id):
        # Retrieve the last known position of a user
        return self.user_positions.get(user_id, "Unknown Position")

# Usage example
sync = UserSync()
sync.update_position("user1", (5, 10, 2))
sync.update_position("user2", (3, 6, 1))
print("User positions:", sync.user_positions)

