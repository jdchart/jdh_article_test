import os
import stat

def init_fluid():
    make_executable(os.path.join(os.getcwd(), "script", "flucoma-cli", "fluid-mfcc"))

def make_executable(file_path):
    if os.path.isfile(file_path):
        st = os.stat(file_path)
        os.chmod(file_path, st.st_mode | stat.S_IEXEC)
        print(f"Made '{file_path}' executable")
    else:
        print(f"File '{file_path}' does not exist")