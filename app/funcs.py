import os
from pathlib import Path

def exit_cmd(args):
    if args not in [None, "", " "]:
        print("Exit command does not accept arguments or trailing spaces")
    else:
        return "exit program"

def echo_cmd(args):
    print(args) 

def type_cmd(args):
    if args in BUILTIN_CMDS.keys():
        print(f"{args} is a shell builtin")
    else:
        found, path = exe_find(args)
        if found:
            print(f"{args} is {path}")
        else:
            print(f"{args}: not found")
        
def exe_find(args):
    path_list = os.environ.get('PATH', '').split(os.pathsep)
    found_path = None
    found = False

    for path_item in path_list:
        check_path = Path(path_item) / args
        if check_path.is_file() and os.access(check_path, os.X_OK):
            found_path = check_path
            found = True
            return found, found_path

    return found, found_path
    

BUILTIN_CMDS = {
    
    "exit":exit_cmd,
    "echo":echo_cmd,
    "type":type_cmd,

    }
