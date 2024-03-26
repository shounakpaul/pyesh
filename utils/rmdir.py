import os


def rmdir(folder_name):
    try:
        os.rmdir(folder_name)
        print(f"Directory '{folder_name}' removed successfully")
        return
    except FileNotFoundError:
        print(f"pyesh: rmdir: cannot remove directory '{
              folder_name}': No such file or directory")
        return
    except PermissionError:
        print(f"pyesh: rmdir: cannot remove directory '{
              folder_name}': Permission denied")
        return
    except OSError:
        print(f"pyesh: rmdir: failed to remove '{
              folder_name}': Directory not empty")
        return
    except Exception:
        print(f"pyesh: rmdir: cannot remove directory '{
              folder_name}': Unexpected error")
        return


if __name__ == "__main__":
    print(rmdir("test"))
