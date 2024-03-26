import os


def touch(file_name):
    try:
        with open(file_name, 'a'):
            os.utime(file_name, None)
        print(f"File '{file_name}' touched successfully")
        return
    except PermissionError:
        print(f"pyesh: touch: cannot touch '{file_name}': Permission denied")
        return
    except Exception:
        print(f"pyesh: touch: cannot touch '{file_name}': Unexpected error")
        return


if __name__ == "__main__":
    touch("test.txt")
