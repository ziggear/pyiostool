import json
import sys

class imgr :
	name=''
	x=''
	y=''
	width=''
	height=''


def parseJSON():
	if len(sys.argv) != 2 :
		print 'Error'
		return False
	else :
		filename = sys.argv[1]
		file = open(filename,'r')
		text = file.read()
		encode = json.loads(text)
		return encode

def checkAndGenerate(jsonobj):
	print jsonobj['frames']

def getImgs():
	imgs = []
	jsonobj = parseJSON()
	if jsonobj == False :
		print 'Exiting'
		return
	else :
		temp = 'frames'
		if (temp in jsonobj) == False:
			print 'Not detected frame data'
			return
		else :
			for single in jsonobj[temp] :
				newimg = imgr()
				if single['name'].endswith('%402x') :
					names = single['name'].split('%402x')
					namestr = names[0]+""
				else :
					namestr = single['name']
				newimg.name = namestr
				newimg.x = single['x']
				newimg.y = single['y']
				newimg.width = single['ow']
				newimg.height = single['oh']
				imgs.append(newimg)
			return imgs

def printImg(image) :
	if isinstance(image,imgr) == False :
		return False
	else :
		print 'name :',image.name
		print 'origin-x:',image.x
		print 'origin-y:',image.y
		print 'width:',image.width
		print 'height:',image.height
	return

def dumpImg(image) :
	if isinstance(image,imgr) == False :
                return False
        else :
		resultStr = "UIImage *%s = [UIImage imageWithCGImage:CGImageCreateWithImageInRect([image CGImage],CGRectMake(%s,%s,%s,%s))];\n" % (image.name,image.x,image.y,image.width,image.height)
		dictStr = "[mainDict setValue:%s forKey:@\"%s\"]" % (image.name,image.name) 
	return resultStr+dictStr

imgarr = getImgs()

for image in imgarr :
	print dumpImg(image)


