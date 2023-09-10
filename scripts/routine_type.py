from enum import Enum

class RoutineType(Enum):
    premade = 0
    custom  = 1

def get_routine_type(mode: str):
    ''' Returns the routine type as supplied by
        the options field in /user_id=<index>/options=<mode>.
        
        Returns invalid if no such mode exists. '''
    
    rout_type   = 0
    for enum_type in (RoutineType):
        if (mode == RoutineType(enum_type.value).name):
            return enum_type
        rout_type   += 1
    else:
        return "invalid"