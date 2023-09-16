class BaseExercise:
    def __init__(self,
                 cooldown: int,
                 img_path: str):
        self.cooldown   = cooldown
        self.img_path   = img_path

    def __repr__(self):
        return " ".join(["Image path:", self.img_path])

_exer_dict  = {}
def add_exercise(exer_name: str, cooldown: int,
                 img_path: str):
    if exer_name in _exer_dict:
        return _exer_dict[exer_name]
    
    _exer_dict[exer_name]   = BaseExercise(cooldown, img_path)
    return _exer_dict[exer_name]

def get_exercise(exer_name: str):
    return _exer_dict[exer_name]