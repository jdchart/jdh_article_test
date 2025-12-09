import os
import stat
import uuid
import scipy
import subprocess

def init_fluid():
    make_executable(os.path.join(os.getcwd(), "script", "flucoma-cli", "fluid-mfcc"))

def make_executable(file_path):
    if os.path.isfile(file_path):
        st = os.stat(file_path)
        os.chmod(file_path, st.st_mode | stat.S_IEXEC)
        print(f"Made '{file_path}' executable")
    else:
        print(f"File '{file_path}' does not exist")

def create_temp():
    os.makedirs(os.path.join(os.getcwd(), ".temp"), exist_ok = True)

def wav_spill(file_path):
    rate, data = scipy.io.wavfile.read(file_path)
    return data

def slicer_test(source):
    create_temp()
    result_file_name = os.path.join(os.getcwd(), ".temp", f"{str(uuid.uuid4()).wav}")
    subprocess.run(["fluid-onsetslice", "-source", source, "-indices", result_file_name])
    result = wav_spill(result_file_name)
    return result