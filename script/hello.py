import os

print("another script")

def test_func(dir_path = os.getcwd()):
    print("Hello World")
    tester2(dir_path)

def tester2(dir_path):
    print(f"cwd : {os.getcwd()}")
    print(f"list of files: {list_files(dir_path)}")

def list_files(dir_path):
    try:
        files = os.listdir(dir_path)
        if not files:
            print(f"No files found in '{dir_path}'")
        else:
            print(f"Contents of '{dir_path}':")
            for f in files:
                print(f" - {f}")
        return files
    except FileNotFoundError:
        print(f"Directory '{dir_path}' does not exist")
        return []