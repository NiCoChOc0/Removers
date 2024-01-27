import os

stuff_to_remove = "[SPOTIFY-DOWNLOADER.COM] "

for filename in os.listdir(os.getcwd()):
    if filename.startswith(stuff_to_remove):
        os.rename(filename,filename[len(stuff_to_remove):])