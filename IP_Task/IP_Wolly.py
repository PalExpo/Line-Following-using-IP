import cv2
import numpy as np
# from Motor import *

# m_1 = Cytron(18, 25)
# m_1 = Cytron(23, 24)
# m_1 = Cytron(20, 12)
# m_1 = Cytron(21, 16)
 
# bot = Base(m_1, m_2, m_3, m_4) 

cap = cv2.VideoCapture(1)

while(1):
	_, frame = cap.read()

	original = frame.copy()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
	close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)


	Kernel_ = cv2.getStructuringElement(cv2.MORPH_RECT, (20,20))
	detect_ = cv2.morphologyEx(close, cv2.MORPH_OPEN, Kernel_, iterations=2)
	counts = cv2.findContours(detect_, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	counts = counts[0] if len(counts) == 2 else counts[1]
	# print(counts[0][0])
	for i in counts:
		for x in i:
			for contour in range(len(counts)):
				area = cv2.contourArea(counts[contour])
				x1,y1,x2,y2 = cv2.boundingRect(counts[contour])
				if area > 20000 and y2 > 400:
					center = x1+(x2/2)
					# print(x[0][0])
					if x[0][0] < [230] and x[0][0] > [120] and (120 < center < 230):
						# bot.antiClockWise()
						print("AntiClock")
					elif x[0][0] > [230] and x[0][0] < [410] and (230 < center < 410):
						# bot.forward() 
						print("forward")
					if x[0][0] > [410] and x[0][0] < [520] and (410 < center < 520):
						# bot.clockWise()
						print("Clock")
					elif x[0][0] > [230] and x[0][0] < [410] and (230 < center < 410):
						# bot.forward() 
						print("forward")

	for count_ in counts:
		cv2.drawContours(original, [count_], -1, (36,255,12), -1)

	original = cv2.line(original, (410, 0), (410, 480), (0,0,255), 10)
	original = cv2.line(original, (230, 0), (230, 480), (0,0,255), 10)
	original = cv2.line(original, (520, 0), (520, 480), (0,0,255), 10)
	original = cv2.line(original, (120, 0), (120, 480), (0,0,255), 10)

	cv2.imshow('original', original)
	if cv2.waitKey(1) & 0xFF == ord("a"):
		break

cap.release()
cv2.destroyAllWindows()
