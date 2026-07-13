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
    all_args = args.split()

    if len(all_args) > 1:
        print("Type command has too many arguments") 
    elif len(all_args) == 0:
        print("Type command requires argument")
    else:
        arg = all_args[0]
        if arg in BUILTIN_CMDS.keys():
            print(f"{arg} is a shell builtin")

        else:
            path_list = os.environ.get('PATH', '').split(os.pathsep)
            found = False

            for path_item in path_list:
                check_path = Path(path_item) / arg
                if check_path.is_file() and os.access(check_path, os.X_OK):
                    print(f"{arg} is {check_path}")
                    found = True
                    
            if not found:
                print(f"{arg}: not found")


BUILTIN_CMDS = {
    
    "exit":exit_cmd,
    "echo":echo_cmd,
    "type":type_cmd,

    }
