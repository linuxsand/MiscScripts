import subprocess
import shutil
import time
import datetime
import os

# 等待某个进程退出后，进行文件的备份和复制操作（实际就是部署新版本的文件）

PROCESS_NAME = "PickWare"

def process_files():
    print("process files...")

    msg = ""
    
    os.chdir("bin-develop")
    dirname = new_dir("dlls-backup--")
    subprocess.check_output("copy /y NE*.dll %s" % dirname, shell=True)
    
    os.chdir("..")
    try:
        subprocess.check_output("move /y NE*.dll bin-develop", shell=True)
        msg = "process_files executed ok"
    except subprocess.CalledProcessError as ex:
        msg = "process_files executed error -- " + str(ex)

    print(msg)
    log_to_file(msg)

    print("process files end")

#########################


def new_dir(prefix = ''):
    x = datetime.datetime.now()
    for i in range(1, 99):
        name = prefix + '{0}{1:02d}{2:02d}-{3}'.format(x.year, x.month, x.day, i)
        if os.path.exists(name): continue
        print('new_dir name is', name)
        os.mkdir(name)
        return name
    return None
        


def log_to_file(msg):
    with open("process_files_for_%s.log" % PROCESS_NAME, "a") as f:
        f.write("%s process_files ran -- " % time.ctime() + msg + "\n")


def assert_process_not_running():
    try:
        ret = subprocess.check_output("wmic process list brief | grep %s" % PROCESS_NAME, shell=True)
#        print(ret)
        return False
    except subprocess.CalledProcessError:
        print("target process [%s] is not running" % PROCESS_NAME)
        return True


def main():
    while not assert_process_not_running():
        time.sleep(1)
        print("wait %s exit..." % PROCESS_NAME)

    process_files()


if __name__ == "__main__":
    main()