import os
import sys
from pathlib import Path
import subprocess

from app.funcs import BUILTIN_CMDS, exe_path

def main():

    while True:
        output_flag = None
        sys.stdout.write("$ ")
        user_input = input()

        if user_input:
            cmd, args = parse_input(user_input)

            if cmd in BUILTIN_CMDS.keys():
                output_flag = BUILTIN_CMDS[cmd](args)

            else: 
                found, path = exe_path(cmd) 

                new_path = [cmd]
                new_path.append(args)
                print("ARGS YOOOOOOOOOOOOOOOOOOOOOOOO: ", args, type(args))

                if found:
                    subprocess.run(new_path)
                else: 
                    print(f"{cmd}: command not found")

        if output_flag == "exit program": 
            break
                

def parse_input(user_input):
    user_in = user_input.split(' ',1)

    if len(user_in) > 1: 
        cmd, args = user_in[0], user_in[1]
    else: 
        cmd, args = user_in[0], None
    return cmd, args


if __name__ == "__main__":
    main()