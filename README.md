## Subtitle Adder

This script will crawl a directory looking for videos. When it finds a video file it will check if the video has
an adjacent caption file or embedded captions.  If it has neither, whisper will be used to generate a 
.vtt caption file. The video files **are not rencoded** the caption file is adjacent to the media file. 

## Dependencies

### ffpmeg
#### On Debian / Ubuntu
```
apt install ffmpeg
```

### whisper
#### Using pip (linux)
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install openai-whisper
```

## Usage
```
usage: main.py [-h] [-d] path

positional arguments:
  path

options:
  -h, --help    show this help message and exit
  -d, --dryrun  Show what files are missing captions
```