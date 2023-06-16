from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
formatter = JSONFormatter()

transcript = YouTubeTranscriptApi.get_transcript('z3fmTwXv1WQ')

# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(transcript)

# Now we can write it out to a file.
with open('your_filename.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)