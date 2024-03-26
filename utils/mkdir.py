import os


def mkdir(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Directory '{folder_name}' created successfully")
        return
    except FileExistsError:
        print(f"pyesh: mkdir: cannot create directory '{
              folder_name}': File exists")
        return
    except PermissionError:
        print(f"pyesh: mkdir: cannot create directory '{
              folder_name}': Permission denied")
        return
    except Exception:
        print(f"pyesh: mkdir: cannot create directory '{
              folder_name}': No such file or directory")
        return


if __name__ == "__main__":
    print(mkdir("test"))
