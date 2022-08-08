import os
import smtplib

raw_command = str(os.popen('netsh wlan show profiles').read())
#define all lists and dictionaries
command_list = raw_command.split()
profiles = []
profile_keys = {

}

#get every word of the list containing the command
for index in range(0, len(command_list)-1):
    if command_list[index] == ':':
        profiles.append(command_list[index+1])
        #now profiles contains every profile this pc has a key to

#now we do a command for every profile that shows the key
for profile in profiles:
    key_command = str(os.popen(f'netsh wlan show profile {profile} key=clear').read())
    key_command_list = key_command.split()
    #get every word of the list again
    for index_2 in range(0, len(key_command_list)-1):
        if key_command_list[index_2] == 'Content':
            #get the word that is 2 indexes after Content and append to dictionary with corrisponding profile
            profile_keys[profile] = str(key_command_list[index_2+2])

print(profile_keys)