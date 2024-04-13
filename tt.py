
import cv2

output_path =  r"C:\Users\archu\Desktop\TASK8\pvideo\video.py"
video_path = r"C:\Users\archu\Downloads\Input Video 2.mp4"
icon_path = r"C:\Users\archu\Pictures\Advertisement Image[517].jpg"

icon_image = cv2.imread(icon_path)


if icon_image is None:
    print("Error: Failed to load icon image.")
    exit()

icon_height, icon_width = 100, 100
icon_x, icon_y = 100, 100


def blend_icon(frame, icon_image, icon_x, icon_y):
   
    icon_image_resized = cv2.resize(icon_image, (icon_width, icon_height))
   
    roi = frame[icon_y:icon_y+icon_height, icon_x:icon_x+icon_width]
  
    blended = cv2.addWeighted(roi, 0.7, icon_image_resized, 0.3, 0)
    frame[icon_y:icon_y+icon_height, icon_x:icon_x+icon_width] = blended
    return frame


video = cv2.VideoCapture(video_path)


if not video.isOpened():
    print("Error: Failed to open video file.")
    exit()


original_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))


new_width = original_width // 2
new_height = original_height // 2

while True:
    
    ret, frame = video.read()
    
    if not ret:
        
        break
    
    
    frame = cv2.resize(frame, (new_width, new_height))
    
   
    frame = blend_icon(frame, icon_image, icon_x, icon_y)
    
   
    cv2.imshow("Video", frame)
    
    
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break


video.release()
cv2.destroyAllWindows()
