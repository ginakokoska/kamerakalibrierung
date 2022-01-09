#Versuch 4
#Grauwertkeil korrigieren:

import cv2
import numpy as np
import matplotlib.pyplot as plt 

eingabeWeissbild = cv2.imread("D:\HTWG\Weissbild.png")
eingabeWeissbild = eingabeWeissbild.astype("double")
normalizedWeiss = eingabeWeissbild / eingabeWeissbild.mean()
eingabebildKorrigiert = cv2.imread("D:\HTWG\SWP.png")
eingabebildKorrigiert =  eingabebildKorrigiert.astype("double")
resultat = eingabebildKorrigiert / normalizedWeiss
resultat = resultat.astype("double")
resultat = cv2.imwrite("D:\HTWG\GrauwertkeilKorrigiert.png", resultat[17:420,7:600,:].astype("uint8"))
#------------------------------------------------------------------------------


#Slicing auf optimale Groesse & Slicing der Grauwertstufen:

GrauwertkeilKorrigiert = cv2.imread("D:\HTWG\GrauwertkeilKorrigiert.png")
GrauwertkeilKorrigiert = GrauwertkeilKorrigiert.astype("double")

black = GrauwertkeilKorrigiert[2:403,5:120,:]
darkgrey = GrauwertkeilKorrigiert[0:403,120:240,:]
midgrey = GrauwertkeilKorrigiert[0:403,242:360,:]
lightgrey = GrauwertkeilKorrigiert[0:403,362:480,:]
white = GrauwertkeilKorrigiert[0:403,484:593,:]
#------------------------------------------------------------------------------


#Errechnen der Werte und Abspeichern in CSV:

import csv
with open('D:\HTWG\grauwerteKorrigiert.csv', mode='w') as file:
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


