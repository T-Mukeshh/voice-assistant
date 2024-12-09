from engine.command import speak
import os
from engine.config import ASSISTANT_NAME


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query !="":
        speak("opening"+ query)
        os.system('start'+ query)
    else:
        speak("not found")