from loader.video_loader import VideoLoader 

import matplotlib.pyplot as plt
import cv2

class RoboPosePipeline:
    def __init__(self, video_path):
        self.loader = VideoLoader(video_path)

    def run(self):
       
        sampled_frames = self.loader.sample_frame(n_frames=20)

        for i, frame in enumerate(sampled_frames):
            # salvar os frames amostrados como imagens
            cv2.imwrite(f"frame_{i:03d}.png", frame)
            
        