import cv2

haar_cascade = 'cars.xml'
video = 'video.avi'
      
cap = cv2.VideoCapture(video) 
car_cascade = cv2.CascadeClassifier(haar_cascade)