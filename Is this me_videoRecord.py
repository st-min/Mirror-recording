import cv2 as cv
import numpy as np

video_file = 0

# Read the given video file
# Note) Additional argument examples
# - Image sequence: video_file = '/PATH'
# - Camera : video_file = 0 (Note: The camera index)
video = cv.VideoCapture(video_file)

if video.isOpened():

    # Configuration for recording
    record_mode = False
    record_file = None
    fourcc = cv.VideoWriter_fourcc(*'MP4V')
    fps = 30.0
    frame_size = (int(video.get(cv.CAP_PROP_FRAME_WIDTH)), int(video.get(cv.CAP_PROP_FRAME_HEIGHT)))
    record_color = (0, 0, 255)

    flip_mode = False

    while True:
        #Read an image from 'video'
        valid, img = video.read()

        if not valid:
            print("Reading ERROR")
            break

        # Horizontal Flip Toggle
        if flip_mode:
            img = cv.flip(img, 1)

        # Recording mode
        if record_mode and record_file is not None:
            record_file.write(img)
            cv.circle(img, (50, 50), 20, record_color, -1)

        #show the image
        cv.imshow('Video Player', img)
        
        # Process the key event
        key = cv.waitKey(1)
        if key == 27:  # ESC 키: 프로그램 종료
            break
        elif key == ord(' '):  # 스페이스 바: 녹화 모드 전환
            record_mode = not record_mode
            if record_mode:
                record_file = cv.VideoWriter('recorded_video.mp4', fourcc, fps, frame_size)
            else:
                record_file.release()
        elif key == ord('1') or key == ord('!'):
            flip_mode = not flip_mode

video.release()
cv.destroyAllWindows()