# 
# Parse HTML web file and insert script in the header <head>
#
import sys
import os
from os import path
scriptFile = ('')
targetFilePath =('')
targetFiles=[]

def main():
    global scriptFile, targetFilePath, targetFiles
    found=0
    try:
        parse_args()
    except TypeError as e:
         print (f'Error:{e}')    
    else:
        #print (targetFiles)
        if path.exists(scriptFile) and path.isfile(scriptFile):
            scriptHandle = open(scriptFile, "r")
            scriptLines = scriptHandle.readlines()
            for i, file in enumerate(targetFiles):
                try:
                    with open(targetFilePath+'/'+file, 'r+') as target_file:
                        print (f"Processing ....:{targetFilePath+'/'+file}")
                        contents = target_file.readlines()
                        for index, line in enumerate(contents): 
                            if line.startswith('<head>'.lower()):
                                index+=1 #place pointer at the next line after the header
                                for i, aline in enumerate (scriptLines):    
                                  contents.insert(index+i, aline)  
                                target_file.seek(0)  
                                target_file.writelines(contents)  
                                found=1
                        if found==0:
                            print ('\n No <head> tag found, not able to add script')          
                except FileNotFoundError as e:
                    print (f'Error:{e}') 
        else:
            print ("Error processing the files")  

def parse_args(*args):
    global scriptFile, targetFilePath
    numargs = len(sys.argv)-1
    if numargs < 3:
        raise TypeError(f'Expected at least 3 argument, got {numargs}')
    scriptFile = sys.argv[1]  #this is the script file
    targetFilePath = sys.argv[2]  #this the directory containing files to edit
    
    for i in range(3, numargs+1): #record all the files to be edited
        targetFiles.append (sys.argv[i])
        

        

    
    
if __name__ == '__main__': main()