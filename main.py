import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)

for i in range(0, 30):
	ret, im = cap.read();

while(True):
	ret, img = cap.read()
	edges = cv2.Canny(img,100,250)

	# plt.subplot(121),plt.imshow(img,cmap = 'gray')
	# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
	# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

	# plt.show()
	# gray = cv2.cvtColor(edges, cv2.COLOR_BGR2GRAY)

	# Display the resulting frame
	cv2.imshow('frame', edges)
	cv2.imshow('frame2', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()