# AutoLabyStreaks
With this tool, you do not have to worry about losing your LabyMod daily log-in streak. This script works on the principle of turning on your PC remotely, running Minecraft on it and turning it back off

This script has been tested on Python 3.9.5 but it should run on 3.x I think.

### 1: 
You need to install minecraft_launcher_lib library first

```bash
pip install minecraft_launcher_lib 
```

### 2:
Enable Wake On Lan packets on your Windows computer, tutorial for that is [here](https://www.howtogeek.com/192642/how-to-remotely-turn-on-your-pc-over-the-internet/)

### 3:
Copy `start.sh` to your server and set a crontab to it
```bash
$ crontab -e
```
add this to the bottom:
```bash
* 3 * * * /path/to/script/start.sh
```

### 4:
Set autologin on Windows for your account [tutorial here](https://www.lifewire.com/how-do-i-auto-login-to-windows-2626066)

### 5:
Compile main.py to main.exeusing pyinstaller  [tutorial here](https://datatofish.com/executable-pyinstaller/)

### 6:
Create `creds.txt` in the same directory as the new main.exe was created and use following format with your Minecraft email & password

```
your_email@example.com///your_password
```

### 7:
Create a shortcut for the main.exe, press Win + R and ether in `shell:startup` and move main.exe to that folder

---


*Note: Your PC will get turned off after MC has been started and the daytime is between 1 and 6 in the morning, you can change it in the script to any other time if you want.*


This is a bit dumb project and it could be probably done in a much better way but meh
