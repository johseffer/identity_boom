import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 boom.py')
    run('mkdir /usr/share/boom')
    run('cp boom.py /usr/share/boom/boom.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/boom/boom.py "$@"')
    with open('/usr/bin/boom','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/boom & chmod +x /usr/share/boom/boom.py')
    print('''\n\ncongratulation Identity BOOM is installed successfully \nfrom now just type \x1b[6;30;42mboom\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/boom ')
    run('rm /usr/bin/boom ')
    print('[!] now Identity BOOM has been removed successfully')
