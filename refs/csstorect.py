# -*- coding:utf-8 -*- #

import os
import re

class image_rect:
    image_name=''
    position=''
    width=''
    height=''
    rectx=0
    recty=0
    rectw=0
    recth=0

fileobj = open('sprites.css','r')
filetext = fileobj.read()

#匹配一个css元素
#.List{
#        background-position: -147px -68px ;
#        width: 29px;
#        height: 29px;
#}

pattern = re.compile(r'(.+?)\{([\s\S.]+?)\}')
match = pattern.match(filetext)
css_elements = pattern.findall(filetext)


#匹配一个元素中的一个key-value值
# [('\n', '\tbackground-position', '\t', ' -147px -68px ', ''), ('\n', '\twidth', '\t', ' 29px', ''), ('\n', '\theight', '\t', ' 29px', '')]
#

pattern = re.compile(r'([\n\r\t\s\S]*?)(([\t\n])[a-zA-Z-]+?):(.+);([\n\t\s\S]*?)')
image_rect_arr = []

for ele in css_elements :
    if len(ele) < 1:
        continue
    else :
        #创建对象
        imgobj = image_rect()
        imgobj.image_name = str(ele[0])

        keyvalue = pattern.findall(str(ele[1]))
        for akey in keyvalue:
            if len(akey) < 3 :
                continue
            else :
                if akey[1] == '\tbackground-position' :
	            imgobj.position = akey[3]
                
		if akey[1] == '\twidth' :
		    imgobj.width = akey[3]
  
		if akey[1] == '\theight' :
                    imgobj.height = akey[3]
	if imgobj.position != '' :
            image_rect_arr.append(imgobj)

print 'all '+str(len(image_rect_arr))+' images'

#显示所有image
# [(' ', '-', '4'), (' ', '-', '49')]
# [(' ', '-', '117')]

pattern = re.compile(r'([\s]*?)([-]*?)([0-9]+)')
for image in image_rect_arr :
    #print 'image name:'+img.image_name
    #print 'image position:'+img.position
    #print 'image width: '+img.width+' image height: '+img.height

    now_position = pattern.findall(image.position)
    image.rectx = int(now_position[0][2])
    image.recty = int(now_position[1][2])

    now_width = pattern.findall(image.width)
    image.rectw = int(now_width[0][2])

    now_height = pattern.findall(image.height)
    image.recth = int(now_height[0][2])

#create file
objc_file_obj = open('code.m','w+')
objc_line = '\nUIImage *image = [UIImage imageNamed:@"sprites.png"]\n'
objc_file_obj.write(objc_line)


for image in image_rect_arr :
    #print 'image: '+image.image_name
    #print 'rect: '+str(image.rectx)+','+str(image.recty)+','+str(image.rectw)+','+str(image.recth)
    objc_line = 'UIImage *%s = [UIImage imageWithCGImage:CGImageCreateWithImageInRect([image CGImage],CGRectMake(%d, %d, %d, %d)];\n\n' % (image.image_name, image.rectx, image.recty, image.rectw, image.recth)
    objc_file_obj.write(objc_line)

objc_file_obj.close()
