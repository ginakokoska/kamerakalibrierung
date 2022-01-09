#Versuch 1 
#Aufnahme eines Grauwertkeils:


import cv2
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow('frame', gray)
    key = cv2.waitKey(1)
    if key%256 == 113:
        break;
grayVal = 0.299*frame[:,:,0] + 0.587*frame[:,:,1]+ 0.114*frame[:,:,2]
photo = cv2.imwrite("D:\HTWG\SWP.png", grayVal.astype("uint8"))
print(photo)
print("frame width:  " + str(cap.get(3)))
print("frame height: " + str(cap.get(4)))
print("brightness:   " + str(cap.get(10)))
print("contrast:     " + str(cap.get(11)))
print("saturation:   " + str(cap.get(12)))
print("gain:         " + str(cap.get(14)))
print("exposure:     " + str(cap.get(15)))
print("white balance:" + str(cap.get(17)))
cap.release()
cv2.destroyAllWindows()
True
frame width:  640.0
frame height: 480.0
brightness:   750.0
contrast:     100.0
saturation:   -1.0
gain:         -1.0
exposure:     -5.0
white balance:-1.0
#------------------------------------------------------------------------------


img = cv2.imread("D:\HTWG\SWP.png")
img = img.astype('double')
plt.imshow(img/255)
immax = img.max()
immin = img.min()
immean = img.mean()
imstd = img.std()
print("Maximaler Grauwert = ", immax)
print("Minimaler Grauwert = ", immin)
print("Mittlerer Grauwert = ", immean)
print("Standardabweichung des Grauwerts = ", imstd)
Maximaler Grauwert =  255.0
Minimaler Grauwert =  23.0
Mittlerer Grauwert =  141.49212565104168
Standardabweichung des Grauwerts =  63.12161776603066
#------------------------------------------------------------------------------


#Slicing auf optimale Groesse & Slicing der Grauwertstufen:

SWPSliced = img[17:420,7:600,:]
plt.imshow(SWPSliced/255)
SWPSliced = cv2.imwrite("D:\HTWG\Grauwertkeil.png", SWPSliced)

Grauwertkeil = cv2.imread("D:\HTWG\Grauwertkeil.png")
Grauwertkeil = Grauwertkeil.astype("double")

black = Grauwertkeil[2:403,5:120,:]
plt.imshow(black/255)

darkgrey = Grauwertkeil[0:403,120:240,:]
plt.imshow(darkgrey/255)

midgrey = Grauwertkeil[0:403,242:360,:]
plt.imshow(midgrey/255)

lightgrey = Grauwertkeil[0:403,362:480,:]
plt.imshow(lightgrey/255)

white = Grauwertkeil[0:403,484:593,:]
plt.imshow(white/255)
#------------------------------------------------------------------------------


#Speichern der Grauwertstufen:

b = cv2.imwrite("D:\HTWG\Schwarz.png", Grauwertkeil[2:403,5:120,:])
d = cv2.imwrite("D:\HTWG\Dunkelgrau.png", Grauwertkeil[0:403,120:240,:])
m = cv2.imwrite("D:\HTWG\Midgrau.png", Grauwertkeil[0:403,242:360,:])
l = cv2.imwrite("D:\HTWG\Hellgrau.png", Grauwertkeil[0:403,362:480,:])
w = cv2.imwrite("D:\HTWG\Weiss.png", Grauwertkeil[0:403,484:593,:]
#------------------------------------------------------------------------------


#Errechnen der Werte und Abspeichern in CSV:

import csv
with open('D:\HTWG\grauwerte.csv', mode='w') as file:
	writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['Grauwertstufe', 'Max', 'Min', 'Mean', 'Std'])

	blackMax  = black.max()
	blackMin = black.min()
	blackMean = black.mean()
	blackStd = black.std()
	writer.writerow(['Schwarz', blackMax, blackMin, blackMean, blackStd])

	darkgreyMax = darkgrey.max()
	darkgreyMin = darkgrey.min()
	darkgreyMean = darkgrey.mean()
	darkgreyStd = darkgrey.std()
	writer.writerow(['Dunkelgrau', darkgreyMax, darkgreyMin, darkgreyMean, darkgreyStd])

	midgreyMax = midgrey.max()
	midgreyMin = midgrey.min()
	midgreyMean = midgrey.mean()
	midgreyStd = midgrey.std()
	writer.writerow(['Mittelgrau', midgreyMax, midgreyMin, midgreyMean, midgreyStd])

	lightgreyMax = lightgrey.max()
	lightgreyMin = lightgrey.min()
	lightgreyMean = lightgrey.mean()
	lightgreyStd = lightgrey.std()
	writer.writerow(['Hellgrau', lightgreyMax, lightgreyMin, lightgreyMean, lightgreyStd])

	whiteMax = white.max()
	whiteMin = white.min()
	whiteMean = white.mean()
	whiteStd = white.std()
	writer.writerow(['Weiss', whiteMax, whiteMin, whiteMean, whiteStd])





