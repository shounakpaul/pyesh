import os
import socket
from utils.pwd import pwd
from utils.mkdir import mkdir
from utils.rmdir import rmdir
from utils.ls import ls
from utils.touch import touch
from utils.cd import cd
from utils.rm import rm


username = os.getlogin()
device_name = socket.gethostname()

current_path = pwd()


def parse_commands(command):
    main_command = command.split(" ")[0]
    second_command = command.split(" ")[1] if len(
        command.split(" ")) > 1 else None
    switcher = {
        "cd": cd,
        "ls": ls,
        "pwd": pwd,  # Don't call the function here
        "mkdir": mkdir,
        "rmdir": rmdir,
        "rm": rm,
        "touch": touch
    }
    try:
        if second_command is not None:
            switcher[main_command](second_command)
        else:
            switcher[main_command]()
    except KeyError:
        os.system(command)
    except FileNotFoundError:
        print(f"pyesh: {main_command}: No such file or directory")
    except FileExistsError:
        print(f"pyesh: {main_command}: File exists")
    except PermissionError:
        print(f"pyesh: {main_command}: Permission denied")
    except Exception:
        print(f"pyesh: {main_command}: command not found")
    finally:
        return


while True:
    print(f"{username}@{device_name}:~$ ", end="")
    terminal_input = input()
    if terminal_input == "exit":
        break
    else:
        parse_commands(terminal_input)
