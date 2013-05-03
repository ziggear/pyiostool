import os

filepath = "./"
pngarr = []

#detect pngcrush exists
path2 = '/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/pngcrush'
path1 = '/usr/local/bin/pngcrush'
binpath = ''

if os.path.isfile(path1) :
    binpath = path1
    print '\n    using pngcrush at '+path1
else :
    if os.path.isfile(path2) :
        binpath = path2
        print '\n    using pngcrush at '+path2
    else :
        print '\n    Error: pngcrush not found\n    Please download it at : http://pmt.sourceforge.net/pngcrush/ \n    Then build the source & copy to /usr/local/bin/ \n'
        exit() 

#canning files 
for root, dirs, files in os.walk(filepath):
    for fn in files :
        if os.path.splitext(fn)[1] == '.png' : 
            pngarr.append(root+'/'+fn)

print '\n    ...scanning '+str(len(pngarr))+' png files \n'

#crushing files! 
options = ' -cc -iphone '
deleteold = True

for file in pngarr:
    os.popen('mv '+file+' '+file+'.old2')
    os.popen(binpath+options+file+'.old2 '+file)
    if deleteold is True :
        os.popen('rm -f '+file+'.old2')

print '\n    Crush Success!\n'


