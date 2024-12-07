import sys

valid_commands = ["exit", "echo", "type"]

def main():
    args = []

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

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        args = input().split(" ")

        # Check user input
        if not args[0] or args[0] not in valid_commands:
            print(f"{args[0]}: command not found")
            continue

        # Run user commands
        if args[0] == "exit":
            cmd_exit()

        if args[0] == "echo":
            cmd_echo()

        if args[0] == "type":
            if args[1] in valid_commands:
                print(f"{args[1]} is a shell builtin")
            else:
                print(f"{args[1]}: not found")

if __name__ == "__main__":
    main()
