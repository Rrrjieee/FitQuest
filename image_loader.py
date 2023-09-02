import base64


# Ripped this snippet from the link provided below:
# https://www.youtube.com/watch?v=pyWqw5yCNdo (Timestamp: 3:58)
def load64(file: str):
    '''
    Loads an image into the web application.
    '''
    with open(file, "rb") as filestream:
        data    = filestream.read()
    return base64.b64encode(data).decode()