# coding: utf-8
"""
    %programfiles%
    %appdata%\roaming
"""

import os
import sys
import shutil
import datetime

print "only run in client os"

WHERE_TO_STORE = "Z:\\D\\npp_backup_" + str(datetime.datetime.now()).split(" ")[0]
FORMAT = "zip"

CLIENT_PROGRAM_PATH = os.environ["programfiles"]
CLIENT_APPDATA_PATH = os.environ["appdata"]
HOST_PROGRAM_PATH = "Z:\\programs"
HOST_APPDATA_PATH = "Z:\\huangjie\\AppData\\Roaming"

FOLDER_PATHS = (HOST_PROGRAM_PATH, HOST_APPDATA_PATH, CLIENT_PROGRAM_PATH, CLIENT_APPDATA_PATH)

print "---------------------"
    
def check_paths():
    return all(map(os.path.exists, 
                   FOLDER_PATHS))
    
def zip_folder(name):
    shutil.make_archive(base_name=name, format=FORMAT, 
                        root_dir=".", base_dir="Notepad++",
                        verbose=1)
    
def backup():
    archive_names = ("host_program",
                     "host_appdata",
                     "client_program",
                     "client_appdata")

    archive_paths = []
    for name, path in zip(archive_names, FOLDER_PATHS):
        print "backup ", name
        os.chdir(path)
        zip_folder(name)   
        archive_paths.append(
            os.path.join(path, name + "." + FORMAT)
        )

    return tuple(archive_paths)
    
    
def move_zips(paths):
    for path in paths:
        shutil.move(path, WHERE_TO_STORE)
    
    
def main():
    if not check_paths():
        print "one or more paths do not exist"
        return
    if not os.path.exists(WHERE_TO_STORE):
        os.mkdir(WHERE_TO_STORE)
        archives = backup()
        move_zips(archives)
    
    
if __name__ == "__main__":
    main()
    import time
    time.sleep(2)
