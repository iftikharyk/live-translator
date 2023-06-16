from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import json
import csv
import pandas as pd
formatter = JSONFormatter()

transcript = YouTubeTranscriptApi.get_transcript('z3fmTwXv1WQ')

# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(transcript)

# Now we can write it out to a file.
with open('your_filename.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)

# try:
#     transcript = YouTubeTranscriptApi.get_transcript('MJEyGsn1C40')
#     # z3fmTwXv1WQ MJEyGsn1C40
# except:
    


print(transcript)

# header = ['text', 'start', 'duration']

# with open('transcript.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=header)
#     writer.writeheader()
#     writer.writerows(transcript)