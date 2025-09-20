import os
import whisper
from moviepy import VideoFileClip
from deep_translator import GoogleTranslator
from gtts import gTTS

# 🔹 BƯỚC 1: Khai báo đường dẫn ffmpeg.exe
ffmpeg_path = r"C:\ffmpeg-2025-09-15-git-16b8a7805b-full_build\ffmpeg-2025-09-15-git-16b8a7805b-full_build\bin\ffmpeg.exe"
os.environ["PATH"] = os.path.dirname(ffmpeg_path) + os.pathsep + os.environ["PATH"]
# ---- ĐƯỜNG DẪN ----
video_path = r"C:\Users\vuchi\Downloads\video.mp4"
audio_path = r"C:\Users\vuchi\OneDrive\Desktop\Python 10\output.wav"
translated_audio_path = r"C:\Users\vuchi\Downloads\chemistry_vi.wav"

# ---- 1. TÁCH ÂM THANH ----
print("🎵 Đang tách audio từ video...")
video = VideoFileClip(video_path)
video.audio.write_audiofile(audio_path, codec="pcm_s16le")

# ---- 2. NHẬN DIỆN TIẾNG ANH ----
print("📝 Đang nhận diện giọng nói...")
model = whisper.load_model("small")
result = model.transcribe(audio_path, task="transcribe", language="en")

# Ghép toàn bộ transcript
full_text_en = " ".join([seg["text"].strip() for seg in result["segments"]])

# ---- 3. DỊCH SANG TIẾNG VIỆT ----
print("🌐 Đang dịch sang tiếng Việt...")
translator = GoogleTranslator(source="en", target="vi")
full_text_vi = translator.translate(full_text_en)

# ---- 4. TTS (chuyển văn bản -> giọng nói) ----
print("🔊 Đang tạo file audio tiếng Việt...")
# Thêm tham số slow=False để tăng tốc độ giọng đọc
tts = gTTS(full_text_vi, lang="vi", slow=False)
tts.save(translated_audio_path)

print("✅ Xong! Có file WAV:", translated_audio_path)