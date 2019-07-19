import speech_recognition as sr
import time
import cv2
import os
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something")
	audio = r.listen(source)
	print("end")
try:
	a = r.recognize_google(audio)
	print("Text: "+ a)
except:
	pass

a  = [i.lower() for i in a.strip().split()]
b = []
for i in range(len(a)):
	if(a[i]=='where' and a[i+1]=='do'):
		b.append('where do')
		continue
	if(a[i]=='do'):
		continue
	b.append(a[i])
for i in a:
	if(i+'.png' in os.listdir('./text to gesture/')):
		x = cv2.imread('./text to gesture/'+i+'.png')
		cv2.imshow('video',x)
		cv2.waitKey(0)
cv2.destroyAllWindows()
