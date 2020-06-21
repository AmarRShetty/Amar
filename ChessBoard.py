import numpy as np
import cv2
board = np.zeros([320,320],dtype = 'uint8')
for i in range(40,320,80):
        for j in range (40,320,80):   
            board[i-40:i,j-40:j] = 255
            board[i:i+40,j:j+40] = 255 
cv2.imshow('Chess Board',board)
cv2.waitKey(0)
cv2.destroyAllWindows()
