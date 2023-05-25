import numpy as np
import cv2
#create a black image
black = np.zeros([600,600])
f_row = black[1:2]
print(f_row)
cv2.imshow("black", black)
cv2.waitKey(0)
