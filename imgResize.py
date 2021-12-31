from PIL import Image, ImageOps
import os 
import PIL 
import glob
import sys
import functools

#sizemodifiers
modThumb=0.12
modSmall=0.25
modMid=0.5
modLarge=0.75


if(len(sys.argv)<4):
	print("usage: imgResize.py inFolder outFolder sizeCode")
	quit()
	

inFolder =str(sys.argv[1])
outFolder = str(sys.argv[2])
sizeCodeCap = str(sys.argv[3])
fileExt=""

#size codes are thumb, small, mid, large [ 1,2,3,4]
if(sizeCodeCap != 'thumb' and sizeCodeCap != 'small' and sizeCodeCap !='mid' and sizeCodeCap !='large' and sizeCodeCap!='all'):
	print ('incorrect size code, options are thumb, small, mid, large')
	quit()
	
#set size modifier
if(sizeCodeCap=='thumb'):
	sizeMod=modThumb
	fileExt ="thumb"
if(sizeCodeCap == 'small'):
	sizeMod = modSmall
	fileExt="small"
if(sizeCodeCap =='mid'):
	sizeMod=modMid
	fileExt="mid"
if(sizeCodeCap == 'large'):
	sizeMod=modLarge
	fileExt="large"

	
#cycle through the folder
for filename in os.listdir(inFolder):
	#check if file is image
	if(filename.endswith(".png") or  filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".webp") ):
		f= os.path.join(inFolder, filename)
		openImg=Image.open(f)
		#workaround
		#openImg.info["exif"] = openImg.getexif()		
		
		img = ImageOps.exif_transpose(openImg)
		width, height = img.size
		
		#are we doing all sizes or one?
		if(sizeCodeCap == 'all'):
			#unroll will just be easier i guess
			#thumb
			outWidth = int(width * modThumb)
			outHeight = int(height * modThumb)
			fileExt="thumb"
			resizedImage = img.resize((outWidth, outHeight))
		
			#write the new image with the new dimensions
			outFile = outFolder+fileExt+"_"+filename
			resizedImage.save(outFile)
			
			#small
			outWidth = int(width * modSmall)
			outHeight = int(height * modSmall)
			fileExt="small"
			resizedImage = img.resize((outWidth, outHeight))
		
			#write the new image with the new dimensions
			outFile = outFolder+fileExt+"_"+filename
			resizedImage.save(outFile)			
			
			#mid
			outWidth = int(width * modMid)
			outHeight = int(height * modMid)
			fileExt="mid"
			resizedImage = img.resize((outWidth, outHeight))
		
			#write the new image with the new dimensions
			outFile = outFolder+fileExt+"_"+filename
			resizedImage.save(outFile)
			
			#large
			outWidth = int(width * modLarge)
			outHeight = int(height * modLarge)
			fileExt="large"
			resizedImage = img.resize((outWidth, outHeight))
		
			#write the new image with the new dimensions
			outFile = outFolder+fileExt+"_"+filename
			resizedImage.save(outFile)
		
		else:
			#set the new size based on the input
			outWidth = int(width * sizeMod)
			outHeight = int(height * sizeMod)
			resizedImage = img.resize((outWidth, outHeight))
			
			#write the new image with the new dimensions
			outFile = outFolder+fileExt+"_"+filename
			resizedImage.save(outFile)
		
