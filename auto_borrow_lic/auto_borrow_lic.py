'''
A tool that automatically borrows KUKA.OfficeLite license from server.
'''

import os, time
from datetime import timedelta, date

# edit fields below
LIC_SERVER = ''
PORT = 2060
DAYS_TO_BORROW = 30

##########################################################################

if DAYS_TO_BORROW < 0 or DAYS_TO_BORROW > 30:
    DAYS_TO_BORROW = 30

UTIL_DIR = 'C:\\KRC\\UTIL\\FLEXLM'
LIC_PATH = str(PORT) + '@' + LIC_SERVER

def check_environ():
    return os.path.exists(UTIL_DIR)

def is_network_ok():
    ret = os.system('ping %s' % LIC_SERVER)
    return ret == 0

def add_lic_file():
    os.system('lmutil.exe lmpath -override LM_LICENSE_FILE %s' % LIC_PATH)
    print '\n\n'

def kill_processes():
    os.system('taskkill /f /im SmartHMI.exe')
    os.system('taskkill /f /im StartKRC.exe')
    print '\n\n'

def return_lic():
    os.system('lmutil.exe lmborrow -return KUKAROB_HMI_8')

def borrow_lic():
    exp_date = get_expire_date()
    print '\nborrow to', exp_date, '\n'
    os.system('lmutil.exe lmborrow KUKAROB %s' % exp_date)

def get_expire_date():
    the_day = date.today() + timedelta(days=DAYS_TO_BORROW)
    return the_day.strftime('%d-%b-%Y')

def start_krc():
    os.system('start C:\\KRC\\StartKRC.exe')

def check_status():
    os.system('lmutil.exe lmborrow -status')
    print '\n\n'

def main():
    if not check_environ():
        print 'FlexLM does not exist'
        return
    os.chdir(UTIL_DIR)
    check_status()
    if not is_network_ok():
        print '\n! Can not reach license server\n\n'
        return
    raw_input('\n\n# Are you ready to go on?\n\n')
    add_lic_file()
    kill_processes()
    return_lic()
    borrow_lic()

if __name__ == '__main__':
    main()
    print 'Only disconnect from license server after KRC started'
    print 'Press <ENTER> to continue...\n'
    raw_input('\nStart KRC...')
    start_krc()
