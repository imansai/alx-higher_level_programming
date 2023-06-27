#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            print(item, end="")
            count += 1
            if count == x:
                break
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        print()
        return count
