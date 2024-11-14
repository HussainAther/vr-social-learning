# group_management.py

class GroupManagement:
    def __init__(self):
        self.groups = {}
        self.roles = {
            "Leader": {"can_create_tasks": True, "can_view_all": True},
            "Member": {"can_create_tasks": False, "can_view_all": True}
        }

    def create_group(self, group_name):
        self.groups[group_name] = {"members": [], "roles": {}}
        print(f"Group '{group_name}' created.")

    def add_user_to_group(self, group_name, user, role="Member"):
        if group_name in self.groups:
            self.groups[group_name]["members"].append(user)
            self.groups[group_name]["roles"][user] = self.roles[role]
            print(f"User '{user}' added to group '{group_name}' with role '{role}'.")
        else:
            print(f"Group '{group_name}' does not exist.")

    def get_user_permissions(self, group_name, user):
        return self.groups[group_name]["roles"].get(user, {})

# Usage example
group_manager = GroupManagement()
group_manager.create_group("Study Group A")
group_manager.add_user_to_group("Study Group A", "Alice", "Leader")
group_manager.add_user_to_group("Study Group A", "Bob", "Member")
print("User Permissions:", group_manager.get_user_permissions("Study Group A", "Alice"))

