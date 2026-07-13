import sys

def exit_cmd(user_input):
    if user_input != "exit":
        return print("exit command does not accept arguments or trailing spaces")
    return "exit"

def echo_cmd(user_input):
    args_to_echo = user_input.split(' ',1)[1]
    print(args_to_echo)
    return 


VALID_COMMANDS = {
    
    "exit":exit_cmd,
    "echo":echo_cmd,

    }
