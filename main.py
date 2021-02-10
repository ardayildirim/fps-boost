import os
from time import sleep
import shutil


def python_files_caller():
    i = 1
    while i <= 4:
        os.system("python " + str(i) + ".py")
        sleep(0.25)
        i += 1


try:
    #first calls for python files
    python_files_caller()

    print("Python files have been run without any error.")

    #remove out directory
    shutil.rmtree("out")
    sleep(0.25)

    #rename akici.mp4 to input.mp4
    os.remove("./input.mp4")
    os.rename('./akici.mp4','./input.mp4')
    sleep(0.25)

    print("out folder is removed and akici.mp4 is renamed to input.mp4")
    print("Calling python files again")

    #again calling python files
    python_files_caller()
    sleep(0.25)
    print("Python files have been run without any error.")
    
    #akici.mp4 is now 60 FPS.
    #removing out folder again.
    print("60 FPS video is ready")
    
    shutil.rmtree("out")
    sleep(0.25)

except Exception:
    print("Error. Here is the error message:")
    print(e)


