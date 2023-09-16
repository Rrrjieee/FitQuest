import glob
import os
from scripts.exercise import add_exercise

def load_exercises():
    exer_list   = []

    # Iterate over the list of files
    for file_path in glob.glob("static/**/*", recursive=True):
        if ((file_path.endswith('/')) or 
            (os.path.isdir(file_path))):
            continue

        file_name   = os.path.basename(file_path).split(".")
        file_ext    = file_name[-1]
        file_name   = file_name[-2]
        if ((file_ext != "png") or (file_name[:9] != "exercise_")):
            continue

        sub_file_path   = "/".join(file_path.split("\\")[1:])
        exer_list.append(
            add_exercise(file_name[10:],
                         20,
                         sub_file_path)
        )

    return exer_list

load_exercises()