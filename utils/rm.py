import os


def rm(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' removed successfully")
        return
    except FileNotFoundError:
        print(f"pyesh: rm: cannot remove '{
              file_name}': No such file or directory")
        return
    except PermissionError:
        print(f"pyesh: rm: cannot remove '{file_name}': Permission denied")
        return
    except IsADirectoryError:
        print(f"pyesh: rm: cannot remove '{file_name}': Is a directory")
        return
    except Exception:
        print(f"pyesh: rm: cannot remove '{file_name}': Unexpected error")
        return


if __name__ == "__main__":
    rm("test.txt")
