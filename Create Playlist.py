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




with open(currentDirectory+'/The_Krabby_Patty Formula_.m3u', "r") as f:
    content_list = [word.strip() for word in f]

""" my_file = open(currentDirectory+'/The_Krabby_Patty Formula_.m3u', "r")
content_list = my_file. readlines() """

# print('playlist contents')
# print(content_list)

musicDirectory
musicWithoutDuplicates = []
duplicatesList = []
count =0
# check for tags equal to none

#musicDirectory =[x for x in musicDirectory j = TinyTag.get(x)  if x != 'wdg']


#remove tracks without albumn artist or title
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
    duplicateL=[]
    duplicateLBiterate=[]
    for duplicate in range(len(musicDirectory)):
        
        duplicateTag = TinyTag.get(musicDirectory[duplicate])
        musicWithoutDuplicates.append(musicDirectory[j])

        if duplicateTag.albumartist == musicDtag.albumartist or duplicateTag.albumartist in musicDtag.albumartist:
            if duplicateTag.title == musicDtag.title or duplicateTag.title in musicDtag.title  :
                #check if last iteration
                if duplicate>=len(musicDirectory)-1:
                    print("found a duplicate!",musicDirectory[duplicate],duplicateTag.albumartist,duplicateTag.title)
                    
                    if len(duplicateLBiterate)==1:## did something here may need to change the conditional statement or add another 
                        print('biterate')
                        #[x for x in duplicateL if TinyTag.get(musicDirectory[x]).bitrate > musicDirectory[x]]
                        print("Current duplicate Bite rate", duplicateLBiterate)                                               
                        for x in range(len(duplicateL)):  
                            if TinyTag.get(duplicateL[x]).bitrate  == max(duplicateLBiterate):
                                #REMOVE ONE WITH THE BEST BITERATE
                                duplicateL.remove(duplicateL[x])
                                print('duplicate list',duplicateL)
                                #Add
                                duplicatesList = duplicatesList + duplicateL
                else:
                    print("found a duplicate!",musicDirectory[duplicate],duplicateTag.albumartist,duplicateTag.title)
                    duplicateL.append(musicDirectory[duplicate])
                    duplicateLBiterate.append(duplicateTag.bitrate)
print('dup ',duplicatesList)

#remove duplicates from list
for u in range(len(duplicatesList)):
    for i in range(len(musicDirectory)):
        if duplicatesList[u]==musicDirectory[i]:
            musicDirectory.remove(musicDirectory[i])
print('music ',musicDirectory)


#create playlist
newPlaylist = open("Test.m3u", "w")


#add file path to the respective track in the new playlist
for content in enumerate(content_list):
    # split strings into artist and title
    trackNumber=content[0]
    trackArray =str(content[1]).split('-')
    albumArtist= trackArray[0].strip()
    title=trackArray[1].strip()
    print('title:',title)
    print('albumArtist:',albumArtist)

    
    for trackDirectory in range(len(musicDirectory)):
        
        trackTag = TinyTag.get(musicDirectory[trackDirectory])
        
        if trackTag.albumartist == albumArtist or trackTag.albumartist in albumArtist:
            if trackTag.title == title or trackTag.title in title:
                newPlaylist.write(trackDirectory + " " + content)
                newPlaylist.close()
                try:
                    while True:
                        content.next()
                except StopIteration:
                    pass

                break
            else:
                print()
        else:
            print()