#Versuch 2
#Aufnahme eines Dunkelbilds:

import cv2
t = 0
s = 0
cap = cv2.VideoCapture(0)
print("frame width:  " + str(cap.get(3)))
print("frame height: " + str(cap.get(4)))
print("brightness:   " + str(cap.get(10)))
print("contrast:     " + str(cap.get(11)))
print("saturation:   " + str(cap.get(12)))
print("gain:         " + str(cap.get(14)))
print("exposure:     " + str(cap.get(15)))
print("white balance:" + str(cap.get(17)))
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key%256 == 113:
        photo = cv2.imwrite("D:\HTWG\Schwarzbild" + str(t) + ".png", frame)
        t = t+1
        print(t)
        if t==10:
            for s in range(10):
                photoRead = cv2.imread("D:\HTWG\Schwarzbild" + str(s) + ".png")
                photoRead = photoRead.astype("double")
                grayVal = 0.299*frame[:,:,0] + 0.587*frame[:,:,1]+ 0.114*frame[:,:,2]
                photoSliced = cv2.imwrite("D:\HTWG\SchwarzbildGrau" + str(s) + ".png", frame)
                s = s+1
            break;
    elif key%256 == 32:
        break;
cap.release()
cv2.destroyAllWindows()
frame width:  640.0
frame height: 480.0
brightness:   750.0
contrast:     100.0
saturation:   -1.0
gain:         -1.0
exposure:     -5.0
white balance:-1.0
#------------------------------------------------------------------------------


#Berechnen und speichern des Mittelwertbildes
import cv2
import matplotlib as plt 
v0 = cv2.imread ("D:\HTWG\SchwarzbildGrau0.png")
v1 = cv2.imread ("D:\HTWG\SchwarzbildGrau1.png")
v2 = cv2.imread ("D:\HTWG\SchwarzbildGrau2.png")
v3 = cv2.imread ("D:\HTWG\SchwarzbildGrau3.png")
v4 = cv2.imread ("D:\HTWG\SchwarzbildGrau4.png")
v5 = cv2.imread ("D:\HTWG\SchwarzbildGrau5.png")
v6 = cv2.imread ("D:\HTWG\SchwarzbildGrau6.png")
v7 = cv2.imread ("D:\HTWG\SchwarzbildGrau7.png")
v8 = cv2.imread ("D:\HTWG\SchwarzbildGrau8.png")
v9 = cv2.imread ("D:\HTWG\SchwarzbildGrau9.png")

v0 = v0.astype("double")
v1 = v1.astype("double")
v2 = v2.astype("double")
v3 = v3.astype("double")
v4 = v4.astype("double")
v5 = v5.astype("double")
v6 = v6.astype("double")
v7 = v7.astype("double")
v8 = v8.astype("double")
v9 = v9.astype("double")

vD = (v0 + v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9)
Dunkelbild = vD / 10.0
DunkelbildKontrast = Dunkelbild * 255.0
photo = cv2.imwrite("D:\HTWG\Dunkelbild.png", Dunkelbild.astype("uint8"))
photo = cv2.imwrite("D:\HTWG\DunkelbildKontrast.png", DunkelbildKontrast.astype("uint8"))
#------------------------------------------------------------------------------


#Einlesen eines Bildes und Subtraktion des Dunkelbildes

import numpy as np
import cv2
import matplotlib as plt
Eingabebild = cv2.imread("D:\HTWG\SWP.png")
Eingabebild = Eingabebild.astype("double")
Dunkelbild = cv2.imread("D:\HTWG\Dunkelbild.png")
Dunkelbild = Dunkelbild.astype("double")
eingabeKorrigiert = Eingabebild - Dunkelbild
cv2.imwrite("D:\HTWG\eingabeKorrigiert.png",eingabeKorrigiert[17:420,7:600,:].astype("uint8"))
