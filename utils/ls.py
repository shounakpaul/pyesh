import os


def ls(directory='.'):
    try:
        files_and_directories = os.listdir(directory)
        for item in files_and_directories:
            print(item)
        return
    except FileNotFoundError:
        print(f"pyesh: ls: cannot access '{
              directory}': No such file or directory")
        return
    except PermissionError:
        print(f"pyesh: ls: cannot open directory '{
              directory}': Permission denied")
        return
    except NotADirectoryError:
        print(f"pyesh: ls: '{directory}': Not a directory")
        return
    except Exception:
        print(f"pyesh: ls: cannot access '{directory}': Unexpected error")
        return


if __name__ == "__main__":
    ls()
