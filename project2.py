import os
import subprocess
import whisper
from googletrans import Translator

# 🔹 BƯỚC 1: Khai báo đường dẫn ffmpeg.exe
ffmpeg_path = r"C:\ffmpeg-2025-09-15-git-16b8a7805b-full_build\ffmpeg-2025-09-15-git-16b8a7805b-full_build\bin\ffmpeg.exe"
os.environ["PATH"] = os.path.dirname(ffmpeg_path) + os.pathsep + os.environ["PATH"]

# 🔹 BƯỚC 2: File video đầu vào
video_path = r"C:\Users\vuchi\Downloads\video.mp4"
audio_path = r"C:\Users\vuchi\OneDrive\Desktop\Python 10\output.wav"

# 🔹 BƯỚC 3: Dùng ffmpeg trích xuất âm thanh WAV
subprocess.run([
    ffmpeg_path, "-i", video_path, "-vn", "-acodec", "pcm_s16le", 
    "-ar", "16000", "-ac", "1", audio_path, "-y"
])

# 🔹 BƯỚC 4: Load model Whisper
model = whisper.load_model("base")

# 🔹 BƯỚC 5: Transcribe audio
result = model.transcribe(audio_path, task="transcribe", language="en")
text_en = result["text"]

print("🎙 Văn bản gốc (English):")
print(text_en)

# 🔹 BƯỚC 6: Dịch sang tiếng Việt
translator = Translator()
translation = translator.translate(text_en, src="en", dest="vi")

print("\n🌍 Bản dịch (Vietnamese):")
print(translation.text)
