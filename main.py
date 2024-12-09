import os 
import eel
from engine.features import *
from engine.command import *


eel.init("www")

os.system('start msedge.exe --app="http://localhost:8000/index.htm"')
playAssistantSound()
eel.start('index.htm', mode=None, host='localhost', block=True)

