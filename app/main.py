import sys
import os
import subprocess
import shlex

valid_commands = ["exit", "echo", "type", "pwd", "cd"]

def main():
    command = None
    args = []
    PATH = os.environ.get("PATH", "").split(":")

    """
    cmd: echo
    """
    def cmd_echo():
        nonlocal args
        print(" ".join(args))

    """
    cmd: exit
    """
    def cmd_exit():
        nonlocal args
        if args and (args[0] == 1 or not args[0]):
            sys.exit(1)
        else:
            sys.exit(0)

    """
    cmd: type
    """
    def cmd_type():
        nonlocal command, args, PATH

        if args[0] in valid_commands: # builtin command
            sys.stdout.write(f"{args[0]} is a shell builtin\n")
        else:
            # Search for command in PATH
            cmd_path = get_executable_path(args[0])
            if cmd_path: # PATH command
                sys.stdout.write(f"{args[0]} is {cmd_path}\n")
            else: # not found
                sys.stdout.write(f"{args[0]}: not found\n")

    """
    cmd: pwd
    """
    def cmd_pwd():
        sys.stdout.write(f"{os.getcwd()}\n")

    """
    cmd: cd
    """
    def cmd_cd():
        nonlocal args

        if not args or not args[0]:
            return

        try:
            path = os.path.expanduser(args[0])
            os.chdir(path)
        except FileNotFoundError:
            sys.stdout.write(f"cd: {args[0]}: No such file or directory\n")
        except NotADirectoryError:
            sys.stdout.write(f"cd: {args[0]}: Not a directory\n")


    # Helper functions

    def get_executable_path(cmd: str):
        nonlocal PATH
        cmd_path = None

        for path in PATH:
            if os.path.isfile(f"{path}/{cmd}"):
                cmd_path = f"{path}/{cmd}"

        return cmd_path

    ##############
    # Main logic #
    ##############
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command, *args = shlex.split(input()) # shlex used to handle single-quotes better

        # Check user input
        if not command:
            continue

        match command:
            case "exit":
                cmd_exit()
            case "echo":
                cmd_echo()
            case "type":
                cmd_type()
            case "pwd":
                cmd_pwd()
            case "cd":
                cmd_cd()
            case _:
                if executable_path := get_executable_path(command):
                    subprocess.run([executable_path, *args])
                else:
                    sys.stdout.write(f"{command}: not found\n")
         


if __name__ == "__main__":
    main()
