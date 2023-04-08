import subprocess
import whisper
import os
from whisper.utils import get_writer

def returnCodeHasCaption(returnCode: int) -> bool:
    if returnCode == 1:
        return False
    else:
        return True

def checkForAdjacentCaption(inputFile: str) -> bool:
    name = os.path.splitext(inputFile)
    captionFile =  "{}.vtt".format(name[0])
    print("Caption File Exists")
    return os.path.isfile(captionFile)

def checkForEmbeddedCaption(inputFile: str) -> bool:
    subtitleCheckCommand = "ffmpeg -i {} -c copy -map 0:s:0 -frames:s 1 -f null - -v 0 -hide_banner".format(inputFile)
    process = subprocess.run(subtitleCheckCommand.split())
    if returnCodeHasCaption(process.returncode):
        print("Embedded Caption Exists")
        return True
    else:
        return False


def checkForCaption(inputFile: str) -> bool:
    return checkForAdjacentCaption(inputFile) or checkForEmbeddedCaption(inputFile)


input = "test.m4v"

if not checkForCaption(input):
    print("Missing Caption...Generating...",end="", flush=True)
    model = whisper.load_model("base")
    writer = get_writer("vtt", os.getcwd())
    result = model.transcribe(input)
    writer(result, input)
    print("Done")



