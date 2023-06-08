#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]  # Exclude the script name from the arguments

    num_args = len(args)
    print("Number of argument(s):", num_args)

    if num_args == 0:
        print(".")
    else:
        print("Arguments:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
