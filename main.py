import subprocess
import whisper
import os
from whisper.utils import get_writer

def returnCodeHasCaption(returnCode: int) -> bool:
    if returnCode == 1:
        return False
    else:
        return True

def checkForCaption(inputFile: str):
    subtitleCheckCommand = "ffmpeg -i {} -c copy -map 0:s:0 -frames:s 1 -f null - -v 0 -hide_banner".format(inputFile)
    process = subprocess.run(subtitleCheckCommand.split())
    
    if returnCodeHasCaption(process.returncode):
        print("Has Caption")
        return True
    else:
        print("No Caption")
        return False

input = "test.m4v"

model = whisper.load_model("base")
writer = get_writer("vtt", os.getcwd())
result = model.transcribe(input)
writer(result, input)



