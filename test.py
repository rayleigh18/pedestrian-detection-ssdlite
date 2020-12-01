import cv2
from imutils import paths
import imutils
import time
from pedestrian_detection_ssdlite import api
from matplotlib import pyplot as plt
import serial

urlPhone = "http://10.128.87.239:8080/video"

# cap = cv2.VideoCapture("test_2.mp4")
# cap = cv2.VideoCapture(0) #for webcam laptop
cap = cv2.VideoCapture(urlPhone)



start = 0
end = 0
fps = 0
count = 0
total_count = 10
total_time = 0

size = (int(cap.get(3)), int(cap.get(4))) # Size Video
dev = serial.Serial("COM17", baudrate=9600) 

result = cv2.VideoWriter('out.avi', cv2.VideoWriter_fourcc(*'MJPG'),10, size)
count_people = 0
while(cap.isOpened()):
    start = time.time()
    berhasil, img = cap.read()
    img = imutils.resize(img, width=min(400, img.shape[1]))
    if berhasil:
        bbox_list = api.get_person_bbox(img, thr=0.6)
        # print(bbox_list)
        last_count = count_people
        count_people = 0

        for i in bbox_list:
            cv2.rectangle(img, i[0], i[1], (125, 255, 51), thickness=2)
            count_people+=1

        #detect People
        if (count_people > 0):
            dev.write(b'1')
        else :
            dev.write(b'0')
        
        text_fps = "FPS =" + str((int)(fps))
        count_people = 0.9*count_people + 0.1*last_count
        text_count = "People ="+str((int)(count_people))

        cv2.putText(img, text_fps, (10,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            1)
        cv2.putText(img, text_count, (120,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            1)

        #Save Image
        cv2.imshow('tracking', img)
        result.write(img)

        # Count FPS
        end = time.time()
        total_time += (end-start)
        if (count < total_count):
            count += 1
        else :
            fps = total_count/total_time
            total_time=0
            count = 0


        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
    else :
        break

#end Procedure
dev.write(b'0')
cap.release()
result.release()
cv2.destroyAllWindows()
