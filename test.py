import cv2
from imutils import paths
import imutils
from pedestrian_detection_ssdlite import api
from matplotlib import pyplot as plt

imagePaths = list(paths.list_images("test_img"))
    
for imagePath in imagePaths:
    img = cv2.imread(imagePath)
    img = imutils.resize(img, width=min(400, img.shape[1]))
    
    bbox_list = api.get_person_bbox(img, thr=0.6)
    print(bbox_list)

    for i in bbox_list:
        cv2.rectangle(img, i[0], i[1], (125, 255, 51), thickness=2)

    plt.imshow(img[:, :, ::-1])
    plt.show()
