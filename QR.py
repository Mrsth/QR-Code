import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import csv

cap = cv2.VideoCapture(0)

data_store = []

while True:
    _,frame = cap.read()

    objects_decoded = pyzbar.decode(frame)
    for obj in objects_decoded:
        myData = obj.data.decode('UTF-8')
        data_store.append(myData)
        myRect_pts = obj.rect
        myPolygon_pts = np.array([obj.polygon],np.int32)

        cv2.polylines(frame,myPolygon_pts,True,(255,0,0),2)
        cv2.putText(frame,myData,(myRect_pts[0],myRect_pts[1]),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,0,0),2)



    cv2.imshow("QRCode",frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(data_store)
print(set(data_store))

with open("QR_csv.csv", 'w', newline='') as file:
    data_writer = csv.writer(file,delimiter=' ')
    data_writer.writerows(set(data_store))