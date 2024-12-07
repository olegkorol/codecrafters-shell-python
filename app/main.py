import sys
import os

valid_commands = ["exit", "echo", "type"]

def main():
    args = []
    PATH = os.environ.get("PATH", "").split(":")

    """
    cmd: echo
    """
    def cmd_echo():
        nonlocal args
        print(" ".join(args[1:]))

    """
    cmd: exit
    """
    def cmd_exit():
        nonlocal args
        if args[1] and args[1] == 1:
            sys.exit(1)
        else:
            sys.exit(0)

    """
    cmd: type
    """
    def cmd_type():
        nonlocal args, PATH

        if args[1] in valid_commands: # builtin command
            sys.stdout.write(f"{args[1]} is a shell builtin\n")
        else:
            # Search for command in PATH
            cmd_path = None
            for path in PATH:
                if os.path.isfile(f"{path}/{args[1]}"):
                    cmd_path = f"{path}/{args[1]}"
            if cmd_path: # PATH command
                sys.stdout.write(f"{args[1]} is {cmd_path}\n")
            else: # not found
                sys.stdout.write(f"{args[1]}: not found\n")

    ##############
    # Main logic #
    ##############
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        args = input().split(" ")

        # Check user input
        if not args[0] or args[0] not in valid_commands:
            sys.stdout.write(f"{args[0]}: command not found\n")
            continue

        # Run user commands
        if args[0] == "exit":
            cmd_exit()

        if args[0] == "echo":
            cmd_echo()

        if args[0] == "type":
            cmd_type()



if __name__ == "__main__":
    main()
