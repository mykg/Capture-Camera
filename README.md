# Capture-Camera
Here i upload some Computer Vision basic programs or codes of small projects. 

#Filter_Camera.py
  import os = to use os(linux i have used) commands
  import cv2 = to import cv module
  cap = cv2.VideoCapture(0)/(1) = to open camera for snap
  grey_color = cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY) = to set filter
  
 #cam_by_myk.py
  import cv2 = to import cv module
  cap = cv2.VideoCapture(0) = to open camera  
  x , photo = cap.read() = to save snap in a variable named as photo
  print(x) = to print value of execution
  cv2.imwrite('/root/Desktop/myphoto.png',photo) = to save snap to a given path
  cap.release() = to release the camera 
