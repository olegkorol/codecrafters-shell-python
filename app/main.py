import sys

valid_commands = ["exit"]

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input().split(" ")

        # Check user input
        if not command[0] or command[0] not in valid_commands:
            print(f"{command[0]}: command not found")
            continue

        if command[0] == "exit":
            if command[1] and command[1] == 1:
                sys.exit(1)
            else:
                sys.exit(0)


if __name__ == "__main__":
    main()
