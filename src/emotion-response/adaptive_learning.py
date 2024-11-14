class AdaptiveLearning:
    def __init__(self, emotion_detector):
        self.emotion_detector = emotion_detector

    def adjust_difficulty(self, emotion):
        if emotion == "frustration":
            print("Detected frustration, reducing difficulty.")
            # Code to lower difficulty or provide a hint
        elif emotion == "joy":
            print("Detected joy, encouraging more challenging tasks.")
            # Code to maintain or increase difficulty
        else:
            print(f"No significant emotion change detected ({emotion}).")

    def provide_feedback(self, emotion):
        if emotion == "frustration":
            print("Offering encouragement: 'You're doing great! Take it step-by-step.'")
        elif emotion == "engagement":
            print("Encouraging: 'Keep up the great work!'")

    def adapt_to_emotion(self, video_frame=None, audio_input=None):
        if video_frame:
            emotion = self.emotion_detector.detect_from_video(video_frame)
            self.adjust_difficulty(emotion)
            self.provide_feedback(emotion)
        elif audio_input:
            emotion = self.emotion_detector.detect_from_audio(audio_input)
            self.adjust_difficulty(emotion)
            self.provide_feedback(emotion)

