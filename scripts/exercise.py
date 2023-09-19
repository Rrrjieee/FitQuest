class BaseExercise:
    def __init__(self,
                 exer_name: str,
                 reps: int,
                 sets: int,
                 img_path: str):
        self.exercise   = exer_name
        self.reps       = reps
        self.sets       = sets
        self.img_path   = img_path

    def __repr__(self):
        return " ".join(["Image path:", self.img_path])

_exer_dict  = {}
def add_exercise(exer_name: str,
                 reps: int,
                 sets: int,
                 img_path: str):
    
    if exer_name in _exer_dict:
        return _exer_dict[exer_name]

    # img_path    = "\\".join(img_path.split("/"))
    img_path    = "".join(['url("', img_path, '")'])
    _exer_dict[exer_name]   = BaseExercise(exer_name, reps, sets, img_path)
    return _exer_dict[exer_name]

def get_exercise(exer_name: str):
    return _exer_dict[exer_name]