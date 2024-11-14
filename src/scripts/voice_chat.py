class Whiteboard:
    def __init__(self):
        self.annotations = []

    def add_annotation(self, user, text):
        annotation = f"{user.name}: {text}"
        self.annotations.append(annotation)
        self.display_annotations()

    def display_annotations(self):
        print("Whiteboard Annotations:")
        for annotation in self.annotations:
            print(annotation)

# Example usage
whiteboard = Whiteboard()
for user in group.users:
    whiteboard.add_annotation(user, "This is a sample annotation.")

