import sys
if sys.platform.startswith('win32'):
    print('This is windows')
elif sys.platform.startswith('linux'):
    print('This is Linux.')#This is a basic installer that's designed to take your input, and create the neccesary files that the discord bot needs in order to function.
import sys
import os
import json
install_path = ''
data = {}
user_input = ''
data['SCRIPT_PATH'] = []
data['LOG_PATH'] = []
if sys.platform.startswith('win32'):
    import subprocess
    print("Windows operating system detected, Proceeding with inital windows Setup.\n")
    while install_path != 'q':
        install_path = input("Do you wish to specify a custom install path or use the default? Please enter Y for yes for New , N for no.\n")
        #If the user chooses Y we ask them to input their path, where we then create the directory. 
        if install_path == 'Y':

            user_input = input("Please enter the path you'd like us to create the file in. \n")
            os.chdir(user_input)
            os.makedirs("Hash_bot")
            user_input = input("What is the path of the script you'd like us to monitor?\n")
            data['SCRIPT_PATH'].append({
                'path': user_input
            })
            user_input = input("What is the log you'd like us to monitor?\n")
            data['LOG_PATH'].append({
                'file_path' : user_input
            })
            with open(r'Hash_bot\file_paths.txt', 'w') as outfile:
                json.dump(data, outfile)
            print('setup successful, thank you.')
            break

        #If the user chooses N we default to just creating the directory in the normal location and moving along. 
        elif install_path == 'N':
            print("Proceeding with initial install. the Default path will be C:\Hash_bot\n")
            os.makedirs("C:\Hash_bot")
            user_input = input("What is the path of the script you'd like us to monitor?\n")
            data['CMD_PATH'].append({
                'path': user_input
            })
            user_input = input("What is the log you'd like us to monitor?\n")
            data['LOG_PATH'].append({
                'file_path' : user_input
            })
            with open(r'C:\Hash_bot\file_paths.txt', 'w') as outfile:
                json.dump(data, outfile)
            print('setup successful, thank you.')
            break
        elif install_path == 'q':
            print("Exiting Program, Thank you.")
        else:
            print('Please enter Y or N')
    

elif sys.platform.startswith('linux'):
    print('Linux Operating System detected, proceeding with initial Linux setup.')
    while install_path != 'q':
        install_path = input("Do you wish to specify a custom install path or use the default? Please enter Y for yes for New , N for no, or q for quit.\n")
        #If the user chooses Y we ask them to input their path, where we then create the directory. 
        if install_path == 'Y':
            user_input = input("Please enter the path you'd like us to create the file in. \n")
            os.chdir(user_input)
            os.makedirs("Hash_bot")
            user_input = input("What is the path of the script you'd like us to monitor?\n")
            data['SCRIPT_PATH'].append({
                'path': user_input
            })
            user_input = input("What is the log you'd like us to monitor?\n")
            data['LOG_PATH'].append({
                'file_path' : user_input
            })
            with open(r'Hash_bot/file_paths.txt', 'w') as outfile:
                json.dump(data, outfile)
            print('setup successful, thank you.')
            break

        #If the user chooses N we default to our Normal install path.
        elif install_path == 'N':
            print("Proceeding with initial install. the Default path will be C:\Hash_bot\n")
            os.makedirs("/usr/local/bin/Hash_bot")
            user_input = input("What is the path of the script you'd like us to monitor?\n")
            data['SCRIPT_PATH'].append({
                'path': user_input
            })
            user_input = input("What is the log you'd like us to monitor?\n")
            data['LOG_PATH'].append({
                'file_path' : user_input
            })
            with open(r'/usr/local/bin/Hash_bot/file_paths.txt', 'w') as outfile:
                json.dump(data, outfile)
            print('setup successful, thank you.')
            break

        #if the user wants to quit
        elif install_path == 'q':
            print("Exiting Program, Thank you.")

        # IF they enter in Values that aren't accepted. 
        else:
            print('Please enter Y or N')
