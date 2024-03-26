# cd.py
import os


def cd(path):
    try:
        os.chdir(path)
        return
    except FileNotFoundError:
        print(f"cd: {path}: No such file or directory")
        return
    except NotADirectoryError:
        print(f"cd: {path}: Not a directory")
        return
    except PermissionError:
        print(f"cd: {path}: Permission denied")
        return


if __name__ == "__main__":
    cd("test")
