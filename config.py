import pwd
import os

# Auto Configuration

def install_requirements():
    try: 
        os.system("sudo pip3 install -r requirements.txt")
        os.system("clear")
    except:
        os.system("sudo pip install -r requirements.txt")
        os.system("clear")
        

def command_sh():
    code = (
    " #!/bin/bash\n\nfunction download() {\n" 
    + f"python3 {os.getcwd()}/downloader.py $1 \n"
    +"}")

    file = open("command.sh","w")
    file.write(code)
    file.close()


def write_bashrc():
    system_username =  pwd.getpwuid(os.getuid())[ 0 ]
    code = f"\nsource {os.getcwd()}/command.sh"
    
    with open(f'/home/{system_username}/.bashrc', 'a') as content:
        content.write(code)
        

if __name__ == "__main__":
    
    # install requirements
    install_requirements()

    # write user into command.sh
    command_sh()

    # install command.sh
    write_bashrc()
