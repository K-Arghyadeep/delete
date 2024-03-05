import os
import shutil



def fn_fe(fi_fo, d_path):
    print(f"Could not find the {fi_fo} in the path: {d_path}")


def pe(fi_fo, d_path):
    print(f"You do not have the permission to remove the {fi_fo}.\npath: {d_path}")


def successful(fi_fo, d_path):
    print(f"{fi_fo} removed from the path: {d_path}")

def rm_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        fn_fe("file", path)
    except PermissionError:
        pe("file", path)
    else:
        successful("file", path)


def rm_dir(path):
    try:
        os.rmdir(path)
    except FileNotFoundError:
        fn_fe("directory", path)
    except PermissionError:
        pe("directory", path)
    except OSError:
        print("Directory not empty. Cannot remove with rm_dir().\nIf you want to remove the directory along with it's content,\nuse rm_tree()")
    else:
        successful("directory", path)


def rm_tree(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        fn_fe("directory", path)
    except PermissionError:
        pe("directory", path)
    else:
        successful("directory", path)


if __name__ == "__main__":
    u_path = "C:\\Users\\kargh\\OneDrive\\Desktop\\practice\\python\\python_basics\\file-handling-python\\Delete\\temp.txt"
    rm_file(u_path)
