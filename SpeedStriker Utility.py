from time import sleep, strftime
from getpass import getuser as username
import datetime
import webbrowser
import os, platform
def skip():
    print("")
def cmdsafe(command):
    try:
        os.system(command)
    except ValueError:
        init()
def exitc(message):
    err = open("err.md","w")
    err.write("SSUTIL ERROR: " +message)
    print("SSUTIL ERROR - SHUTDOWN INITIATED")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("2...")
    sleep(1)
    webbrowser.open("https://cdn.rawgit.com/SpeedStriker243/ssutil/c356c899/SSUTILE.html")
    exit()
os.system("color 0b")
if platform.release() == "8" or platform.release() == "8.1" or platform.release() == "10":
    name = "PC"
elif platform.release() != "Vista":
    name = "computer"
else:
    name = "outdated piece of junk"
selected = 0
print("Starting SpeedStriker Utility...")
cmdsafe("title Loading...")
sleep(3)
if str(platform.system()) != "Windows":
    exitc("SpeedStriker Utility requires Microsoft Windows.")
skip()
cmdsafe("title SpeedStriker Utility - " +str(platform.system()) + " " + str(platform.release())+ " - " +str(strftime("%a, %d %b %Y")))
print("SpeedStriker Utility on " +str(platform.system()) , str(platform.release())+ ".")
print(str(strftime("%a, %d %b %Y, %H:%M.")))
hide = 0
def init():
    global hide
    def scan_dir(path):
        print(list(map(os.path.abspath, os.listdir(pwd))))
    cwd = os.getcwd()
    if hide == 0:
        prompt = input(cwd + " | ssutil> ")
    elif hide == 1:
        prompt = input("ssutil> ")
    elif hide == 2:
        prompt = input(cwd + "> ")
    elif hide == 3:
        prompt = input("> ")
    
    if prompt[:2] == "cd":
        try:
            os.chdir(prompt[3:])
        except FileNotFoundError:
            print("Unable to find the specified file.")
            init()
        except OSError:
            print("No directory was specified.")
            init()

    if prompt[:7] == "pccheck":
        os.system("systeminfo |find \"OS\"")
        os.system("systeminfo |find \"Memory\"")

    if prompt[:2] == "up":
        os.chdir("..")
        
    if prompt[:4] == "echo":
        print(prompt[5:])
        
    if prompt[:2] == "ls":
       for dirname, dirnames, filenames in os.walk('.'):

        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))
            
        for filename in filenames:
            print(os.path.join(dirname, filename))

        if '.git' in dirnames:
            dirnames.remove('.git')
        init()

    if prompt[:3] == "new":
        os.system("mkdir " + prompt[4:])
        init()

    if prompt[:3] == "del":
        os.system("del " + prompt[4:])

    if prompt[:5] == "crash":
        exitc("The end-user manually crashed the utility.")

    if prompt == "help":
        skip()
        print("Command List:")
        print("su - Opens a Command Prompt (not SSUTIL) window with your current user privileges")
        print("netsu [servername] - Possesses the same function as su, but for use if your computer is on a network.")
        print("psu - Opens a PowerShell window with your current user privileges")
        print("netpsu [servername] - Possesses the same function as psu, but for use if your computer is on a network.")
        print("sudo [command] - Runs any CMD command with your current user privileges")
        print("pccheck - Displays information about your "+name)
        print("clear/cls - Clears the screen")
        print("prompt [nothing|path|ssutil|all] - Affects the visibility of elements of the prompt")
        print("cd [dirname] - Changes your current directory")
        print("path - Gets and prints the current path")
        print("copypath - Copies the current path to the clipboard")
        print("ls - Lists directories")
        print("up - Goes up a directory")
        print("open - Opens the specified file")
        print("echo [message] - Prints a message to the console")
        print("new [dirname] - Creates a new directory")
        print("del [filename] - Deletes the specified file")
        print("web [URL] - Opens the specified URL in your browser")
        print("wsearch [search term] - Searches the web for the specified search term")
        print("exit - Gracefully exits the utility")
        print("crash - Invokes an SSUTIL crash.")
        skip()
        init()

    if prompt[:6] == "prompt":
        if prompt[7:] == "all":
            hide = 0
        if prompt[7:] == "ssutil":
            hide = 1
        if prompt[7:] == "path":
            hide = 2
        if prompt[7:] == "nothing":
            hide = 3
        init()

    if prompt[:4] == "open":
        cmdsafe("start " + prompt[5:])

    if prompt[:3] == "web":
        if prompt[4:] == "":
            print("The command was typed improperly.")
            print("Usage: web [URL]")
        else:
            webbrowser.open(str(prompt[4:]))
        init()

    if prompt[:7] == "wsearch":
        if prompt[8:] == "":
            print("The command was typed improperly.")
            print("Usage: wsearch [search term]")
        else:
            if str(platform.system()) == "Windows":
                webbrowser.open("www.bing.com/search?q=" + prompt[8:])
            else:
                webbrowser.open("www.google.com/search?q=" + prompt[8:])

    if prompt[:3] == "cmd":
        os.system(prompt[4:])
        init()

    if prompt[:5] == "clear":
        if str(platform.system()) == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        init()

    if prompt[:3] == "cls":
        if str(platform.system()) == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        init()

    if prompt[:4] == "path":
        print(os.getcwd())
        init()

    if prompt[:4] == "exit":
        try:
            quit()
        except EOFError:
            print("")

    if prompt[:4] == "sudo":
        if prompt[5:] == "":
            print("The command was typed improperly.")
            print("Usage: sudo [command]")
            init()
        cmdsafe("runas /noprofile /user:" +platform.node()+"\\" +username()+ " " + prompt[5:])
        init()

    if prompt[:2] == "su":
        cmdsafe("runas /noprofile /user:" +platform.node()+"\\" +username()+ " cmd")
        init()

    if prompt[:5] == "netsu":
        cmdsafe("runas /noprofile /user:" +prompt[6:]+"\\" +username()+ " cmd")
        init()

    if prompt[:3] == "psu":
        cmdsafe("runas /noprofile /user:" +platform.node()+"\\" +username()+ " powershell")
        init()

    if prompt[:6] == "netpsu":
        cmdsafe("runas /noprofile /user:" +prompt[7:]+"\\" +username()+ " powershell")
        init()

    if prompt[:8] == "copypath":
        cmdsafe("echo " + os.getcwd().strip() + "| clip")

    if prompt == None:
        init()

    else:
        init()
init()
