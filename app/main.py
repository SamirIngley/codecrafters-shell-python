import sys
from app.funcs import VALID_COMMANDS

def main():

    while True:
        sys.stdout.write("$ ")
        command = input()

        if command:
            if command not in VALID_COMMANDS.keys():
                print(f"{command}: command not found")
            else: 
                output_flag = VALID_COMMANDS[command]()

                if output_flag == "exit": 
                    break
                
        


if __name__ == "__main__":
    main()