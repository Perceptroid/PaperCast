from supabase import create_client, Client
import os

# Supabase credentials
SUPABASE_URL = "url"
SUPABASE_KEY = "key'
BUCKET_NAME = "name"

# Files to upload
AUDIO_FILE_PATH = "output/audio.wav"
THUMBNAIL_FILE_PATH = "output/thumbnail.jpg" 

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Function to upload a file
def upload_to_supabase(file_path, dest_path):
    with open(file_path, "rb") as f:
        file_data = f.read()

    response = supabase.storage.from_(BUCKET_NAME).upload(
        path=dest_path,
        file=file_data,
        file_options={"content-type": "application/octet-stream", "upsert": True}
    )
    if "error" in response:
        print(f"❌ Failed to upload {file_path}: {response['error']['message']}")
    else:
        print(f"✅ Uploaded {file_path} as {dest_path}")

# Upload audio and thumbnail
upload_to_supabase(AUDIO_FILE_PATH, "episodes/audio.wav")
upload_to_supabase(THUMBNAIL_FILE_PATH, "thumbnails/thumbnail.jpg")
