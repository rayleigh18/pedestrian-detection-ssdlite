import cv2
from imutils import paths
import imutils
import time
from pedestrian_detection_ssdlite import api
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

start = 0
end = 0
fps = 0
count = 0
total_count = 10
total_time = 0

while(1):
    start = time.time()
    berhasil, img = cap.read()
    img = imutils.resize(img, width=min(400, img.shape[1]))

    bbox_list = api.get_person_bbox(img, thr=0.6)
    # print(bbox_list)
    for i in bbox_list:
        cv2.rectangle(img, i[0], i[1], (125, 255, 51), thickness=2)
    text_fps = "FPS =" + str((int)(fps))
    cv2.putText(img, text_fps, (10,50),
    cv2.FONT_HERSHEY_SIMPLEX,
     0.5,
     (0, 0, 0),
     1)
    cv2.imshow('tracking', img)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
    end = time.time()
    total_time += (end-start)
    if (count < total_count):
        count += 1
    else :
        fps = total_count/total_time
        total_time=0
        count = 0
        print(fps)
# imagePaths = list(paths.list_images("test_img"))
    
# for imagePath in imagePaths:
#     img = cv2.imread(imagePath)
#     img = imutils.resize(img, width=min(400, img.shape[1]))
    
#     bbox_list = api.get_person_bbox(img, thr=0.6)
#     print(bbox_list)

#     for i in bbox_list:
#         cv2.rectangle(img, i[0], i[1], (125, 255, 51), thickness=2)

#     plt.imshow(img[:, :, ::-1])
#     plt.show()
