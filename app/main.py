import sys

valid_commands = ['cd']

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        if command not in valid_commands:
            print(f"{command}: command not found")
            continue


if __name__ == "__main__":
    main()
