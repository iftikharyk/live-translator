from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.formatters import WebVTTFormatter
from youtube_transcript_api.formatters import SRTFormatter
import csv
import pandas as pd
jsonFormatter = JSONFormatter()
srtFormatter = SRTFormatter()
    

def saveAsJSON(dict):
    # .format_transcript(transcript) turns the transcript into a JSON string.
    json_formatted = jsonFormatter.format_transcript(dict)

    # Now we can write it out to a file.
    with open('your_filename.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_formatted)

def saveAsSRT(dict):
    srt_formatted = srtFormatter.format_transcript(dict)

    with open('subtitles.srt', 'w', encoding='utf-8') as srt_file:
        srt_file.write(srt_formatted)

def saveAsCSV(dict):
    header = ['text', 'start', 'duration']

    with open('transcript.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(dict)

def saveAsTXT(dict):
    with open('example.txt', 'w') as file:
        for obj in dict:
            file.write(obj['text'] + '\n')

def loadTranscript(videoId):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(videoId)

        saveAsJSON(transcript)
        saveAsCSV(transcript)
        saveAsTXT(transcript)
        saveAsSRT(transcript)
        print('Done')
    
    except:
        print('Error')
    

#contains transcript
loadTranscript('z3fmTwXv1WQ')

#does not contains transcript
# loadTranscript('MJEyGsn1C40')