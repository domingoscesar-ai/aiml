	
from ultralytics import YOLO
import cv2
 
# Load the YOLO26 pose model (auto-downloads on first run)
model = YOLO("yolo26n-pose.pt")
 
def run_keypoint_on_image(image_path, output_path="./ComputerVision/data/img/yoga.png", conf=0.5):
    """Run YOLO26 keypoint estimation on a single image."""
    results = model(image_path, conf=conf)
 
    for result in results:
        # Draw skeleton + keypoints on image
        annotated_frame = result.plot()
        cv2.imwrite(output_path, annotated_frame)
 
        # Print keypoint info
        if result.keypoints is not None:
            keypoints = result.keypoints.xy  # shape: (N_persons, 17, 2)
            print(f"Detected {len(keypoints)} person(s)")
            print(f"Keypoints shape: {keypoints.shape}")
 
    return results
 
if __name__ == "__main__":
    run_keypoint_on_image("./data/img/yoga2.png", output_path="./data/img/output_image.png")
    

    """
    5.3 Accessing Raw Keypoint Data

KEYPOINT_NAMES = [
    "Nose", "Left Eye", "Right Eye", "Left Ear", "Right Ear",
    "Left Shoulder", "Right Shoulder", "Left Elbow", "Right Elbow",
    "Left Wrist", "Right Wrist", "Left Hip", "Right Hip",
    "Left Knee", "Right Knee", "Left Ankle", "Right Ankle",
]
 
results = model("karate.png", conf=0.5)
 
for result in results:
    if result.keypoints is None:
        continue
    for person_idx, kps in enumerate(result.keypoints.xy):
        print(f"\n--- Person {person_idx + 1} ---")
        for i, (x, y) in enumerate(kps):
            if x > 0 and y > 0:
                conf_score = result.keypoints.conf[person_idx][i].item()
                print(f"  {KEYPOINT_NAMES[i]:20s}: ({x:.1f}, {y:.1f})  conf={conf_score:.3f}")
                

    5.4 Multi-Person Detection
    
from ultralytics import YOLO
import cv2
 
# Load the YOLO26 pose model
model = YOLO("yolo26n-pose.pt")
 
def run_keypoint_on_video(video_path, output_path="output_video.mp4", conf=0.5):
    Run YOLO26 keypoint estimation on a video file frame by frame.
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video '{video_path}'")
        return
 
    fps    = int(cap.get(cv2.CAP_PROP_FPS))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total  = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
 
    print(f"Processing : {video_path}")
    print(f"Resolution : {width}x{height} @ {fps}fps | {total} total frames")
 
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
 
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
 
        results = model(frame, conf=conf, verbose=False)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)
 
        frame_count += 1
        if frame_count % 30 == 0:
            print(f"  Processed {frame_count}/{total} frames...")
 
    cap.release()
    out.release()
    print(f"Done! Output saved to: {output_path}")
 
if __name__ == "__main__":
    run_keypoint_on_video("dance.mp4", output_path="output_dance.mp4")
    """