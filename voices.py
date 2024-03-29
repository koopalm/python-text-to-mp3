import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get the available voices
voices = engine.getProperty('voices')

# Print information about each voice
for idx, voice in enumerate(voices):
    print(f"Voice {idx + 1}:")
    print(" - ID:", voice.id)
    print(" - Name:", voice.name)
    print()

# Select the first available voice
if voices:
    selected_voice = voices[0]
    print("Selected Voice:")
    print(" - ID:", selected_voice.id)
    print(" - Name:", selected_voice.name)
else:
    print("No voices found.")
