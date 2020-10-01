import os
import shutil

print (os.getcwd())

#get current working directory
cwd = os.getcwd()
#get the list of dirctories and file inside cwd
files = os.listdir(cwd)

#create neccessary folders if not present
if 'Documents' not in files:
    os.makedirs("./Documents/")
if 'Images' not in files:
    os.makedirs("./Images/")
if 'Videos' not in files:
    os.makedirs("./Videos/")
if 'Compressed' not in files:
    os.makedirs("./Compressed/")
if 'Programs' not in files:
    os.makedirs("./Programs/")
if 'Audio' not in files:
    os.makedirs("./Audio/")
if 'Other' not in files:
    os.makedirs("./Other/")

#list of all audio extension
audioExt = ['aif', 'cda','mid','midi','mp3','mpa','ogg','wav','wma','wpl']
#list of all compressed file extenstion
compressedExt = ['7z','arj','deb','pkg','rar','rpm','gz','z','zip']
#list of all documents extension
documentsExt = ['md','doc','odt','rtf','tex','txt','wpd','csv','dat','db','log','sql','xml','pdf','pps','pptx','ppt','odp','key','xls','ods','xlsm','xlsx','cfg','tmp','sys','ini']
#list of all video extension
videoExt = ['3g2','3gp','avi','flv','h264','m4v','mkv','mov','mp4','mpg','rm','swf','vob','wmv']
#list of all image extension
imageExt = ['ai','bmp','gif','ico','jpeg','png','ps','jpg','psd','svg','tif','tiff','xpm']
#list of all program extension
programExt = ['apk','bat','bin','cgi','pl','com','exe','gadget','jar','msi','py','wsf']

#loop throug all the files in current directory
for file in files:
    fileExtension = file.split(".")
    if len(fileExtension) >= 2 :
        print (fileExtension[len(fileExtension) - 1])
        fileExtension = fileExtension[len(fileExtension) - 1]
        if file != 'fileOrganizer.py':
            if fileExtension in audioExt:
                oldPath = os.path.join(cwd, file)
                newPath = os.path.join(cwd, "Audio", file)
                os.replace(oldPath, newPath)
            elif fileExtension in imageExt:
                oldPath = os.path.join(cwd, file)
                newPath = os.path.join(cwd, "Images", file)
                os.replace(oldPath, newPath)
            elif fileExtension in videoExt:
                oldPath = os.path.join(cwd, file)
                newPath = os.path.join(cwd, "Videos", file)
                os.replace(oldPath, newPath)
            elif fileExtension in compressedExt:
                oldPath = os.path.join(cwd, file)
                newPath = os.path.join(cwd, "Compressed", file)
                os.replace(oldPath, newPath)
            elif fileExtension in programExt:
                oldPath = os.path.join(cwd, file)
                newPath = os.path.join(cwd, "Programs", file)
                os.replace(oldPath, newPath)
            elif fileExtension in documentsExt:
                oldPath = os.path.join(cwd, file)
                newPath = os.path.join(cwd, "Documents", file)
                os.replace(oldPath, newPath)
            else:
                oldPath = os.path.join(cwd, file)
                newPath = os.path.join(cwd, "Other", file)
                os.replace(oldPath, newPath)
