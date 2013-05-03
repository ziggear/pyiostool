import os
import re

#Common Vars
gl_verbose = True
gl_workingDir="./"

#Common Functions
def xcodeReady():
    pipe = os.popen('xcodebuild clean')
    if gl_verbose :
    	print pipe.readlines()
    pipe = os.popen('export DEVELOPER_DIR=$DEVELOPER_DIR:/Applications/Xcode.app/Contents/Developer')
    if gl_verbose :
        print pipe.readlines()

def isExistProject():
    dirArr = os.listdir(gl_workingDir)
    pattern = re.compile(r'(.+).xcode')
    for filename in dirArr:
        match = pattern.match(filename)
        if match :
            return match.group(1)
    return False

#Project Class
class Project:
    project_dir=""
    project_name=""
    product_name=""
    code_sign=""
    arch=""
    version=""


