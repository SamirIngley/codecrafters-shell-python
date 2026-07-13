import sys

def exit_cmd(args):
    if args not in [None, "", " "]:
        print("exit command does not accept arguments or trailing spaces")
    else:
        return "exit"

def echo_cmd(args):
    print(args) 

def type_cmd(args):
    all_args = args.split()

    if len(all_args) > 1:
        print("Too many arguments") 
    elif len(all_args) == 0:
        print("Type command requires argument")
    else:
        arg = all_args[0]
        if arg in BUILTIN_CMDS.keys():
            print(f"{arg} is a shell builtin")
        else:
            print(f"{arg}: not found")


BUILTIN_CMDS = {
    
    "exit":exit_cmd,
    "echo":echo_cmd,
    "type":type_cmd,

    }
