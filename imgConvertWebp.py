from PIL import Image, ImageOps
import os 
import PIL 
import glob
import sys
import functools


if(len(sys.argv)<3):
	print("usage: imgResize.py inFolder outFolder ")
	quit()
	

inFolder =str(sys.argv[1])
outFolder = str(sys.argv[2])

	

	
#cycle through the folder
for filename in os.listdir(inFolder):
	#check if file is image
	if(filename.endswith(".png") or  filename.endswith(".jpg") or filename.endswith(".jpeg") ):
		f= os.path.join(inFolder, filename)
		openImg=Image.open(f)		
		img = ImageOps.exif_transpose(openImg)		
		#change file extension
		fn = os.path.splitext(filename)
			
		#write the new image with the new dimensions
		outFile = outFolder+fn[0]+".webp"
		img.save(outFile)

