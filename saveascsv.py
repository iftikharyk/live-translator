from youtube_transcript_api import YouTubeTranscriptApi
import csv

transcript = YouTubeTranscriptApi.get_transcript('z3fmTwXv1WQ')

header = ['text', 'start', 'duration']

with open('transcript.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(transcript)