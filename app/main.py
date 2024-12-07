import sys

valid_commands = ["exit", "echo"]

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

        if command[0] == "echo":
            print_string_from_list(command[1::])

def print_string_from_list(lst: list):
    str = ""
    for word in lst:
        if not lst[-1] == word:
            str += word + " "
        else:
            str += word
    print(f"{str}")

if __name__ == "__main__":
    main()
