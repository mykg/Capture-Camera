import os

os.system("tput setaf 1")
print("\t\twelcome to my filter")
os.system("tput setaf 0")
print("\t\t------------------")

while True:
	print("""
		press 1: to open BGR face cam
		press 2: to open grayscale face cam
		press 3: to open LAB face cam
		press 4: to open HSV face cam
		press 5: to open LUV face cam
		press 6: to open RGB face cam
		press 7: to open YUV face cam
		""")
	print("Enter your choice : ",end='')
	ch=input()
	print(ch)
	if   int(ch) == 1:
		import cv2
		cap = cv2.VideoCapture(0)
		while True:
			x , photo = cap.read()
			cv2.imshow("this is live streaming",photo)
			if cv2.waitKey(1) == 13:
				break
		cv2.destroyAllWindows()
		cap.release()

	elif int(ch) == 2:
		import cv2

		cap = cv2.VideoCapture(0)
		while True:
			x , photo = cap.read()
			grey_color = cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
			cv2.imshow("this is a live stream",grey_color)
			if cv2.waitKey(1) == 13:
				break

		cv2.destroyAllWindows()
		cap.release()

	elif int(ch) == 3:
		import cv2

		cap = cv2.VideoCapture(0)
		while True:
			x , photo = cap.read()
			grey_color = cv2.cvtColor(photo,cv2.COLOR_BGR2Lab)
			cv2.imshow("this is a live stream",grey_color)
			if cv2.waitKey(1) == 13:
				break

		cv2.destroyAllWindows()
		cap.release()
				 
	elif int(ch) == 4:
		import cv2

		cap = cv2.VideoCapture(0)
		while True:
			x , photo = cap.read()
			grey_color = cv2.cvtColor(photo,cv2.COLOR_BGR2HSV)
			cv2.imshow("this is a live stream",grey_color)
			if cv2.waitKey(1) == 13:
				break

		cv2.destroyAllWindows()
		cap.release()
	elif int(ch) == 5:
		import cv2

		cap = cv2.VideoCapture(0)
		while True:
			x , photo = cap.read()
			grey_color = cv2.cvtColor(photo,cv2.COLOR_BGR2LUV)
			cv2.imshow("this is a live stream",grey_color)
			if cv2.waitKey(1) == 13:
				break

		cv2.destroyAllWindows()
		cap.release()
	elif int (ch) == 6:
		import cv2

		cap = cv2.VideoCapture(0)
		while True:
			x , photo = cap.read()
			grey_color = cv2.cvtColor(photo,cv2.COLOR_BGR2RGB)
			cv2.imshow("this is a live stream",grey_color)
			if cv2.waitKey(1) == 13:
				break

		cv2.destroyAllWindows()
		cap.release()
	elif int (ch) == 7:
		import cv2

		cap = cv2.VideoCapture(0)
		while True:
			x , photo = cap.read()
			grey_color = cv2.cvtColor(photo,cv2.COLOR_BGR2YUV)
			cv2.imshow("this is a live stream",grey_color)
			if cv2.waitKey(1) == 13:
				break

		cv2.destroyAllWindows()
		cap.release()

	else: 
		print("command does not exists")
	input("press enter to continue")
