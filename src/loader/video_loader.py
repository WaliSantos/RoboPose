import cv2
import numpy as np

class VideoLoader:
    def __init__(self, path):
        self.cap = cv2.VideoCapture(path)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return ret, frame
    
    def release(self):
        self.cap.release()

    def sample_frame(self, n_frames = 20):
        total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"Total de frames do video: {total_frames}")

        indices = np.linspace(0, total_frames - 1, n_frames, dtype=int)

        sampled_frames = []
        for idx in indices:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, idx) # move para o frame desejado
            ret, frame = self.cap.read()
            if ret:
                sampled_frames.append(frame)
        
        print(f"Frames amostrados: {len(sampled_frames)}")

        return sampled_frames
    