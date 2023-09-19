import glob
import os
import json
from scripts.exercise import add_exercise

def load_exercises():
    exer_list   = []
    
    json_file   = open("exercises_config.json")
    file_dict   = json.load(json_file)
    json_file.close()

    for entry in file_dict:
        entry_dict  = file_dict[entry]
        exer_list.append(
            add_exercise(entry,
                         entry_dict['reps'],
                         entry_dict['sets'],
                         entry_dict['img_path'])
        )

    return exer_list