import os
import re
from elevenlabs import generate, save, set_api_key


set_api_key("sk_fd4efee02578e8c222ec51c2f97d96cc9b4170abbfe687ca") 
# Voice mapping (speaker -> ElevenLabs voice)
voice_map = {
    "Alex": "Adam",    # Male
    "Maya": "Rachel",  # Female
}

# Load script from file
with open("script.txt", "r", encoding="utf-8") as f:
    raw_script = f.read()

def convert_to_voice_tagged(script: str, voice_map: dict) -> str:
    # Replace speaker tags with <voice> tags
    def replacer(match):
        speaker = match.group(1).strip()
        text = match.group(2).strip()
        voice_name = voice_map.get(speaker, "Adam")  # Default to Adam
        return f'<voice name="{voice_name}">{text}</voice>'

    # Replace **Host X (Name):** TEXT with voice tags
    pattern = re.compile(r"\*\*Host \d+ \((.*?)\):\*\* (.+)")
    tagged = pattern.sub(replacer, script)

    # Remove stage directions like **(Intro Music fades in)**
    tagged = re.sub(r"\*\*.*?\*\*", "", tagged)

    return tagged.strip()

# Convert the script
voice_script = convert_to_voice_tagged(raw_script, voice_map)

# Save the tagged script for reference
with open("voice_script.txt", "w", encoding="utf-8") as f:
    f.write(voice_script)

# Generate audio
audio = generate(
    text=voice_script,
    model="eleven_multilingual_v2",
    voice="Adam",  # Placeholder, overridden by <voice> tags
    output_format="mp3"
)

# Save the audio
save(audio, "model_insights_episode1.mp3")
print("✅ Audio saved as model_insights_episode1.mp3")
print("📝 Tagged script saved as voice_script.txt")
