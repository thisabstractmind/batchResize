<pre>
# batchResize
python script to resize images into different sizes for websites, linux CLI

usage:python3 imgResize.py inFolder outFolder sizeCode

inFolder = destination where original full size images are stored
outFolder = location to put new images (this will not be made automatically, must be created first)
sizeCode = Code that is used for selecting the new size for the output images
Codes are:
thumb - 12% of original image size
small - 25% of original image size
mid - 50% of original image size
large - 75% of original image size
all - performs all resizing operations 

all images will be prepended with their respective resize. i.e. 001.jpg -> small_001.jpg
</pre>
