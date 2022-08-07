import os

raw_command = str(os.popen('netsh wlan show profiles').read())
command_list = raw_command.split()
profiles = []
keys = []
profile_keys = {

}

for index in range(0, len(command_list)-1):
    if command_list[index] == ':':
        profiles.append(command_list[index+1])

for profile in profiles:
    key_command = str(os.popen(f'netsh wlan show profile {profile} key=clear').read())
    key_command_list = key_command.split()
    for index_2 in range(0, len(key_command_list)-1):
        if key_command_list[index_2] == 'Content':
            keys.append(str(key_command_list[index_2+2]))
            profile_keys[profile] = str(key_command_list[index_2+2])

print(profile_keys)