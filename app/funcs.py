import os
from pathlib import Path

def cd_cmd(args):
    target_dir = Path(str(args))
    # can be absolute path or not absolute path I think? 
    if target_dir.is_dir():
        os.chdir(target_dir)
    elif args == "~":
        os.chdir(Path.home())
    else: 
        print(f"cd: {target_dir}: No such file or directory")


def exit_cmd(args):
    if args:
        print("Exit command does not accept arguments or trailing spaces")
    else:
        return "exit program"

def echo_cmd(args):
    print(args) 

def exe_path(exe):
    path_list = os.environ.get('PATH', '').split(os.pathsep)
    found_path = None

    for path_item in path_list:
        check_path = Path(path_item) / exe
        if check_path.is_file() and os.access(check_path, os.X_OK):
            found_path = check_path
            return found_path

    return found_path

def help_cmd(args):
    if args:
        print("Help command does not accept arguments or trailing spaces")
    else:
        print("\nBuiltin Commands: ", *(item for item in BUILTIN_CMDS.keys()), sep='\n')
        print("\n")

def pwd_cmd(args):
    current_working_directory = Path.cwd()
    print(current_working_directory)

def type_cmd(arg):
    if arg in BUILTIN_CMDS.keys():
        print(f"{arg} is a shell builtin")
    else:
        path = exe_path(arg)
        if path:
            print(f"{arg} is {path}")
        else:
            print(f"{arg}: not found")


BUILTIN_CMDS = {

    "cd":cd_cmd,
    "exit":exit_cmd,
    "echo":echo_cmd,
    "help":help_cmd,
    "pwd":pwd_cmd,
    "type":type_cmd,

    }
