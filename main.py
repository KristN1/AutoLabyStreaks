import time
import os
import datetime
import subprocess
import minecraft_launcher_lib

now = datetime.datetime.now()
print(now.hour)

if now.hour > 1 and now.hour < 6:

    with open("creds.txt", "r") as f:

        line = f.readline()
        line_split = line.split("///")
        email = line_split[0]
        password = line_split[1]

    login_data = minecraft_launcher_lib.account.login_user(email, password)
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

    #Get Minecraft command
    options = {
        "username": login_data["selectedProfile"]["name"],
        "uuid": login_data["selectedProfile"]["id"],
        "token": login_data["accessToken"],
        "server": "play.cubecraft.net",
    }

    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("LabyMod-3-1.16.5",minecraft_directory,options)
    try:
        mc = subprocess.call(minecraft_command, timeout=25)
    except subprocess.TimeoutExpired:
        pass # dump error

    minecraft_launcher_lib.account.logout_user(email, password)

    print("done")
    time.sleep(3)

    os.system("shutdown /s /t 1")
