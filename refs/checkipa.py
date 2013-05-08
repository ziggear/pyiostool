import os
import sys
import re

def checkfilename(file):
	if os.path.isfile(file) == False :
		print 'File not exist!'
		return False	

	namelist = file.split('.')
	pos = len(namelist)-1
	if namelist[pos] == 'ipa' :
		print 'Yes, this is an ipa filename'
		return True
	else :
		print 'This isn\'t ipa file, aborting...'
		return False

def checkpackage(file):
	namelist = file.split('.ipa')
	filename = namelist[0]
	fullname = file
	
	os.system('rm -f '+filename+'.zip')
	os.system('mv '+fullname+' '+filename+'.zip')
	os.popen('unzip -o -d temp/'+filename+'/ '+filename+'.zip')
	os.system('mv '+filename+'.zip '+fullname)	

	targetnamelist = file.split('_')	
	targetname = targetnamelist[0]
	binary = 'temp/'+filename+'/Payload/'+targetname+'.app/'+targetname
	print '>>> match binary:'
	print '>>> '+binary
	return binary

def checkbinary(file, binfile) :
	if os.path.isfile(binfile) == False :
		print 'Binary not found'
		return False
	else :
		targetnamelist = file.split('_')
        	targetname = targetnamelist[0]
		results = os.popen('strings '+binfile+' | grep \''+targetname.lower()+'\'')
		
		firstline = results.readline()	
		print '>>> match line:'
		print '>>> '+firstline
		
	return firstline

def checkchannel(file, matchline) :
	#
	namelist = file.split('.ipa')
        filename = namelist[0]
	#
	targetnamelist = filename.split('_')
        targetname = targetnamelist[0]
	devicename = targetnamelist[1]
	channelname = targetnamelist[2]
	version = targetnamelist[3]
	
	print 'target = '+targetname
	print 'device = '+devicename
	print 'channel = '+channelname
	
	print matchline
	pattern = re.compile(r'(.+?)_(.+?)_(.+)')
	result = pattern.findall(matchline)

	if False :
		print '>>> Previous Error : ChannelID didn\'t match'
		return False
	else :
		res = result[0]
		bin_target = res[0]
		bin_device = res[1]
		bin_channel = res[2]

	
	print '>>> Now matching ......'+bin_channel
	if bin_target == targetname.lower() :
		print '>>> target name match:'+bin_target+' -- '+targetname
		if bin_device == devicename :
			print '>>> device name match:'+bin_device+' -- '+devicename
			if bin_channel == channelname :
				print '>>> channel name match: '+bin_channel+' -- '+channelname
				return True
		else :
			return False
	else :
		return False
	
def cleantemp() :
	os.popen('rm -rf temp')		

def check() :
	os.system('mkdir temp')
	os.system('chmod 755 -R temp')

	if (len(sys.argv) == 2) :
		ipafile = sys.argv[1]
		if checkfilename(ipafile) is True:
			bin = checkpackage(ipafile)
			matchline = checkbinary(ipafile, bin)
			if checkchannel(ipafile, matchline) == True :
				print '>>> Congradulations! Match Channel Success!'
				cleantemp()
				return True
		else :
			cleantemp()
			return False

	else :
		print 'error input'
		print 'usage: python checkipa.py XXX.ipa'
		return False


check()
