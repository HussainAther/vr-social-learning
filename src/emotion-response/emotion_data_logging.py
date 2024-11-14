import time
import json

class EmotionDataLogger:
    def __init__(self, emotion_detector):
        self.emotion_detector = emotion_detector
        self.data_log = []

    def log_data(self):
        # Collect emotional data for each session
        self.data_log.append({
            "timestamp": time.time(),
            "emotion": self.emotion_detector.current_emotion
        })

    def save_log(self, filename="emotion_data_log.json"):
        with open(filename, "w") as file:
            json.dump(self.data_log, file)
        print(f"Emotion data log saved to {filename}.")

# Visualization example (basic plot for data log analysis)
import matplotlib.pyplot as plt

class EmotionVisualizer:
    def __init__(self, data_log):
        self.data_log = data_log

    def plot_emotion_over_time(self):
        timestamps = [entry["timestamp"] for entry in self.data_log]
        emotions = [entry["emotion"] for entry in self.data_log]
        
        plt.plot(timestamps, emotions, marker='o')
        plt.xlabel("Time")
        plt.ylabel("Emotion State")
        plt.title("Emotion States Over Time")
        plt.show()

# Usage example
logger = EmotionDataLogger(emotion_detector=EmotionDetection())
# Collect and log data during VR session
logger.log_data()
# Save the log
logger.save_log()

# Load and visualize
visualizer = EmotionVisualizer(data_log=logger.data_log)
visualizer.plot_emotion_over_time()

