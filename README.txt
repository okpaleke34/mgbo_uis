


START CRON JOB 
$ sudo service cron start
VERIFY CRON JOB
$ sudo service cron status

LINUX SUBSYSTEM: kali-linux

------

pip freeze > requirements.txt

pip install -r requirements.txt

LINUX/WINDOWS
* * * * * cd /mnt/c/Users/okpal/Documents/SEM5/mgbo_uis/ && /usr/bin/python3 /mnt/c/Users/okpal/Documents/SEM5/mgbo_uis/set_progress.py  >> /mnt/c/Users/okpal/Documents/SEM5/mgbo_uis/log_progress.txt 2>&1
* * * * * cd /mnt/c/Users/okpal/Documents/SEM5/mgbo_uis/ && /usr/bin/python3 /mnt/c/Users/okpal/Documents/SEM5/mgbo_uis/main.py  >> /mnt/c/Users/okpal/Documents/SEM5/mgbo_uis/log_main.txt 2>&1

MAC
* * * * * cd /Users/okpaleke34/Documents/programming/mgbo_uis/ && /usr/local/bin/python3 /Users/okpaleke34/Documents/programming/mgbo_uis/set_progress.py  >> /Users/okpaleke34/Documents/programming/mgbo_uis/log_progress.txt 2>&1
* * * * * cd /Users/okpaleke34/Documents/programming/mgbo_uis/ && /usr/local/bin/python3 /Users/okpaleke34/Documents/programming/mgbo_uis/main.py  >> /Users/okpaleke34/Documents/programming/mgbo_uis/log_main.txt 2>&1




wsl -l -v
wsl --list
wsl --setdefault DISTRO-NAME


NANO
    Ctrl + O: Write Out (save)
    Confirm the filename or provide a new one if needed.
    Press Enter to confirm.
    Ctrl + X: Exit nano.
VIM SAVE
    Press "Esc"
    Type ":wq"
    OR 
    Press "Esc"
    Type ":w"
    Press Enter
    Type ":q!"

---------

C:\Program Files\Python39\python.exe
C:\Users\okpal\Documents\SEM5\mgbo_uis

0251450312 514864751 2110942502


# ALGORITHM
    # 1. Get what is in the clipboard
    # 2. Verify if its an answer, question for chatgpt, getting content of a file
    # 3. If its an answer, question for chatgpt, getting content of a file, then do the necessary
    # 4. If its not, then append to the clipboard content(...Error: wrong formatting[]) and then copy it to the clipboard
    # 5. always save the clipboard content to a csv file for future reference. Timestamp, content, type of content, etc
    # 6. If its ->{getting content of a file}, then get the content of the file and copy it to the clipboard
    # 7. If its =>{question for chatgpt}, put loading... in the clipboard and search for it using chatgpt api
    # 8. If its &>{answer}, just leave it there