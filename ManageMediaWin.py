import os
import shutil
import datetime

# 1. List out all the files inside your folder
source_path ='''C:\\Users\\mengn\\Downloads\\testphoto\\'''
dest_path='''C:\\Users\\mengn\\Downloads\\sortedfiles\\'''
names = os.listdir(source_path)


# 2. Create two new folders
folder_name = ['Photos', 'Movies']
for x in range(0,2):
    if not os.path.exists(dest_path+folder_name[x]):
        os.makedirs(dest_path+folder_name[x])

# 3. Create subfolders based on filename extensions and dates
photo_type = ['.JPG', '.ARW', '.DNG', '.PNG']
movie_type = ['.MP4', '.MOV']

for ptype in photo_type:
    for files in names:
    # getmtime is date modified
    # getctime is date created
        cdate = datetime.datetime.fromtimestamp(os.path.getmtime(source_path+files)).strftime('%Y%m%d')
        ext = os.path.splitext(files)[1]
        if ext.upper() == ptype and not os.path.exists(dest_path+'Photos\\'+ptype[1:]+'\\'+cdate):
            os.makedirs(dest_path+'Photos\\'+ptype[1:]+'\\'+cdate)
            

for mtype in movie_type:
    for files in names:
    # getmtime is date modified
    # getctime is date created
        cdate = datetime.datetime.fromtimestamp(os.path.getmtime(source_path+files)).strftime('%Y%m%d')
        ext = os.path.splitext(files)[1]
        if ext.upper() == mtype and not os.path.exists(dest_path+'Movies\\'+mtype[1:]+'\\'+cdate):
            os.makedirs(dest_path+'Movies\\'+mtype[1:]+'\\'+cdate)


# 4. Copy files into the folders and add prefix
for files in names:
    cdate = datetime.datetime.fromtimestamp(os.path.getmtime(source_path+files)).strftime('%Y%m%d')
    ext = os.path.splitext(files)[1]
    # save photos
    for ptype in photo_type:
        pref = 'IMG_'
        if ext.upper() == ptype and not os.path.exists(dest_path+'Photos\\'+ptype[1:]+'\\'+cdate+'\\'+pref+files):
            shutil.copy2(source_path+files, dest_path+'Photos\\'+ptype[1:]+'\\'+cdate+'\\'+pref+files)
    # save movies
    for mtype in movie_type:
        pref = 'MOV_'
        if ext.upper() == mtype and not os.path.exists(dest_path+'Movies\\'+mtype[1:]+'\\'+cdate+'\\'+pref+files):
            shutil.copy2(source_path+files, dest_path+'Movies\\'+mtype[1:]+'\\'+cdate+'\\'+pref+files)


