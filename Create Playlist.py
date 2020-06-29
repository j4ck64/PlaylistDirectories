import os
import glob
import shutil
from tinytag import TinyTag

""" root = 'C:/'
copy_to = '/copy to/folder'
tag = TinyTag.get('C:/Users/jchap/OneDrive/Pictures/(VERYRAREBOYZ) (feat. $ki Mask The Slump God and Drugz).mp3')
print(tag.artist)
print('song duration: '+str(tag.duration))
 """

f = []
f=glob.glob('C:/Users/jchap/OneDrive/*.mp3')
print(f)

musicDirectory=[]
musicFiles =[]
# tag = TinyTag.get(f[0])
# print(tag.artist)

# for root, dirs, files in os.walk("C:/Users/jchap/OneDrive/"):
for root, dirs, files in os.walk("C:/"):
    for file in files:
        if file.endswith(".mp3"):
             musicFiles.append(file)
             musicDirectory.append(os.path.join(root, file))
             #print(os.path.join(root, file))

print('files'+str(musicFiles))
tag = TinyTag.get(musicDirectory[0])
print('Artist',tag.artist)
print('Album Artist',tag.albumartist)
print('Title',tag.title)
print('Biterate',tag.bitrate)

print('music directory'+str(musicDirectory))
print(len(musicDirectory))

currentDirectory =os.path.dirname(__file__)



my_file = open(currentDirectory+'/The_Krabby_Patty Formula_.m3u', "r")
content_list = my_file. readlines()
# print('playlist contents')
# print(content_list)

musicDirectory
musicWithoutDuplicates = []
duplicatesList = []
count =0
# check for tags equal to none

#musicDirectory =[x for x in musicDirectory j = TinyTag.get(x)  if x != 'wdg']

for track in reversed(range(len(musicDirectory))):
    try:
        trackTag = TinyTag.get(musicDirectory[track])    
        if str(trackTag.albumartist)== 'None' or str(trackTag.title)=='None':
            print('albumArtist = none',musicDirectory[track]) 
            print('removing track and adding to log file')
            musicDirectory.remove(musicDirectory[track])
    except IndexError:
        break

    




#check for duplicates
for j in range(len(musicDirectory)):
    musicDtag = TinyTag.get(musicDirectory[j])
    for duplicate in range(len(musicDirectory)):

        duplicateTag = TinyTag.get(musicDirectory[duplicate])
        musicWithoutDuplicates.append(musicDirectory[j])

        if duplicateTag.albumartist == musicDtag.albumartist:
            if duplicateTag.title == musicDtag.title:
                if duplicateTag.bitrate>=musicDtag.bitrate:
                    duplicatesList.append(musicDirectory[duplicate])
                    print("found a duplicate!",musicDirectory[duplicate],duplicateTag.albumartist,duplicateTag.title)

print(duplicatesList)

for u in range(len(duplicatesList)):
    for i in range(len(musicDirectory)):
        if duplicatesList[u]==musicDirectory[i]:
            musicDirectory.remove(musicDirectory[i])
            
