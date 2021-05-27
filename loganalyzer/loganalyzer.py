# Michael Jarnling <email>

# IMPORTS
import sys

# CONTANTS
str_error = "error"
str_notice = "notice"

#### Script
### Usage: python loganalyzer.py filepath action
## valid actions: statistics, error, notice

### filepath
## take in a valid filepath, check if exists, open it, otherwise - return error
# test.log

def openfile(filepath): 
    try:
        file = open(filepath, "r")
    except FileNotFoundError:
        str_exit = "Could not open the specified file: "+filepath
        sys.exit(str_exit)
    else:
        global lines
        lines = file.read().split('\n')
        file.close()

### statistics
## output:
# errors 340
# notice 450
## where the first value is the type of log entry and the second value is the number of such entries there are in the file

def stats():
    error_count = 0
    notice_count = 0
    for line in lines:
        if str_error in line:
            error_count += 1
        elif str_notice in line:
            notice_count += 1
        else:
            continue

    print("errors", error_count)
    print("notice", notice_count)

### error
## prints the 'error' messages in the file with each row as follows:
# date message

def fetch_error():
    for line in lines:
        if str_error in line:
            line = line.split("[error]")
            date = line[0]
            msg = line[1]
            print(date,msg)
        else:
            continue

### notice
## prints the 'notice' messages in the file with each row as follows:
# date message

def fetch_notice():
    for line in lines:
        if str_notice in line:
            line = line.split("[notice]")
            date = line[0]
            msg = line[1]
            print(date,msg)
        else:
            continue

## Assign parameters
# check if there are 3 parameters (scriptname, filepath and action)
if len(sys.argv) == 3:
    # filepath
    fpath=str(sys.argv[1])
    openfile(fpath)
    # action
    action=str(sys.argv[2])
    # check which action
    if action == "statistics":
        stats()
    elif action == "error":
        fetch_error()
    elif action == "notice":
        fetch_notice()
    else:
        print("No valid action specified (statistics, error, notice)")
else:
    print("Not enough or invalid amount of parameters specified. \nRequires: filepath action (statistics, error, notice)")