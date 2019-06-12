import cv2
cap = cv2.VideoCapture(0)
x , photo = cap.read()
print(x)
cv2.imwrite('/root/Desktop/myphoto.png',photo)
cap.release()
