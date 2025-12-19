import mediapipe as mp
import cv2 as cv

class hand_detector():
    def __init__(self, static_image_mode = False, 
                    model_complexity = 0,
                    min_detection_confidence = 0.7,
                    min_tracking_confidence = 0.9):
        
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode = static_image_mode, 
                                        model_complexity = model_complexity,
                                        min_detection_confidence = min_detection_confidence,
                                        min_tracking_confidence = min_tracking_confidence )
    
    def find_hands(self, frame, draw = True):
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(frame_rgb)
        
        if draw:
            if self.results.multi_hand_landmarks:
                for hand_landmarks in self.results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(frame, hand_landmarks, 
                                                self.mp_hands.HAND_CONNECTIONS)
        return frame
    
    def find_position(self, frame, id = 8, draw = True):
        landmark_list = []
        hand_status = [0, 0]
         
        if self.results.multi_hand_landmarks and self.results.multi_handedness:
                
            for hand_landmarks, handedness in zip(self.results.multi_hand_landmarks, self.results.multi_handedness):
                # hand status
                hand_type = 0 if handedness.classification[0].label == "Left" else 1
                hand_status[hand_type] = 1 # [1, 1]
                
                # landmarks
                for index, landmark in enumerate(hand_landmarks.landmark):
                    hight, width, channels = frame.shape
                    x_center, y_center = int(landmark.x * width), int(landmark.y * hight)
                    landmark_list.append([index, x_center, y_center, hand_type])
                    if draw and index == id:
                        cv.circle(frame, (x_center, y_center), 9, (255, 0, 255), cv.FILLED)
                    
        return landmark_list, hand_status
    
def main():
    capture = cv.VideoCapture(0)
    detector = hand_detector()
    
    while True:
        success, frame = capture.read()
        frame = detector.find_hands(frame)
        landmark_list, hand_status = detector.find_position(frame)
        
        if len(landmark_list) != 0:
            print(f"Hand status: {landmark_list[8]}")
        
        cv.imshow('hand_tracking', cv.flip(frame, 1))
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    capture.release()

if __name__ == "__main__":
    main()
                    
                    