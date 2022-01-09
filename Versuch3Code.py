#Versuch 3
#Aufnahme eines Weissbildes:


import numpy as np
import cv2
import matplotlib as plt
#----------------------------------------------------------

t = 0
s = 0
cap = cv2.VideoCapture(0)
cap.set(15, cap.get(12)*0.4)
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
        photo = cv2.imwrite("D:\HTWG\WP" + str(t) + ".png", frame.astype("uint8"))
        t = t+1
        print(t)
        if t==10:
            for s in range(10):
                photoRead = cv2.imread("D:\HTWG\WP" + str(s) + ".png")
		photoRead = photoRead.astype("double")
                frameSliced = photoRead[0:390,0:640,:]
                grayVal = 0.299*frameSliced[:,:,0] + 0.587*frameSliced[:,:,1]+ 0.114*frameSliced[:,:,2]
                photoSliced = cv2.imwrite("D:\HTWG\WPSLICED" + str(s) + ".png", grayVal.astype("uint8"))
                s = s+1
            break;
    elif key%256 == 32:
        break;
cap.release()
cv2.destroyAllWindows()
#----------------------------------------------------------


w0 = cv2.imread("D:\HTWG\WPSLICED0.png")
w1 = cv2.imread("D:\HTWG\WPSLICED1.png")
w2 = cv2.imread("D:\HTWG\WPSLICED2.png")
w3 = cv2.imread("D:\HTWG\WPSLICED3.png")
w4 = cv2.imread("D:\HTWG\WPSLICED4.png")
w5 = cv2.imread("D:\HTWG\WPSLICED5.png")
w6 = cv2.imread("D:\HTWG\WPSLICED6.png")
w7 = cv2.imread("D:\HTWG\WPSLICED7.png")
w8 = cv2.imread("D:\HTWG\WPSLICED8.png")
w9 = cv2.imread("D:\HTWG\WPSLICED9.png")

w0 = w0.astype("double")
w1 = w1.astype("double")
w2 = w2.astype("double")
w3 = w3.astype("double")
w4 = w4.astype("double")
w5 = w5.astype("double")
w6 = w6.astype("double")
w7 = w7.astype("double")
w8 = w8.astype("double")
w9 = w9.astype("double")

wAdd = w0 + w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9
wMittelwertbild = wAdd / 10.0
Dunkelbild = cv2.imread("D:\HTWG\Dunkelbild.png")
Dunkelbild = Dunkelbild.astype("double")
Weissbild = wMittelwertbild - Dunkelbild
#cv2.imshow("wAdd", wAdd)
#cv2.imshow("Mittel", wMittelwertbild)
#cv2.imshow("Dunkel", Dunkelbild)
#cv2.imshow("Weiss", Weissbild)
cv2.waitKey()
WeissbildKontrast = (Weissbild / Weissbild.max()) * 255.0
WeissbildKontrast = cv2.imwrite("D:\HTWG\WeissbildKontrast.png", WeissbildKontrast.astype("uint8"))
Weissbild = cv2.imwrite("D:\HTWG\Weissbild.png", Weissbild.astype("uint8"))
#----------------------------------------------------------


eingabeWeissbild = cv2.imread("D:\HTWG\Weissbild.png")
eingabeWeissbild = eingabeWeissbild.astype("double")
normalizedWeiss = eingabeWeissbild / eingabeWeissbild.mean()
eingabebildKorrigiert = cv2.imread("D:\HTWG\eingabeKorrigiert.png")
eingabebildKorrigiert =  eingabebildKorrigiert.astype("double")
resultat = eingabebildKorrigiert / normalizedWeiss
resultat = resultat.astype("double")
resultat = cv2.imwrite("D:\HTWG\Resultat.png", resultat.astype("uint8"))

frame width:  640.0
frame height: 480.0
brightness:   750.0
contrast:     100.0
saturation:   -1.0
gain:         -1.0
exposure:     -5.0
white balance:-1.0

153.47557291666666
0.9999999999999996
