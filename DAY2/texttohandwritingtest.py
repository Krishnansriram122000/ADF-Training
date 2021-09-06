import cv2
import numpy as np
from PIL import Image

a=np.ones([6898,7000,3],np.uint8)
a*=255
imagelist=[]
h=open('daaass3.txt','r+').read()
i=0
j=0
for t in h:
	try:
		if t==' ':
			b=cv2.imread('letters\\space.jpg')
		elif t=='\t':
			b=cv2.imread('letters\\tab.jpg')
		elif t=='.':
			b=cv2.imread('letters\\fs.jpg')
		elif t=='?':
			b=cv2.imread('letters\\qm.jpg')
		elif t=='"':
			b=cv2.imread('letters\\quote.jpg')
		elif ord(t)>64 and ord(t)<91:
			b=cv2.imread('letters\\'+t+'.png')
		elif t=="\n":
			i+=180
			j=0
			continue
		else:
			b=cv2.imread('letters\\'+t+'.jpg')
		try:
			hei,wid,chan=b.shape
		except AttributeError:
			print(t)
			break
		print(hei,wid)
		try:
			a[i:i+hei,j:j+wid]=b
		except ValueError:
			i+=hei+50
			j=0
			a[i:i+hei,j:j+wid]=b
		j+=wid
	except Exception:
		cv2.imwrite("Assignment3.jpg",a)
		image1=Image.open("Assignment3.jpg")
		im1=image1.convert('RGB')
		imagelist.append(im1)
		a=np.ones([6898,7000,3],np.uint8)
		a*=255
		i=0
		j=0


		

