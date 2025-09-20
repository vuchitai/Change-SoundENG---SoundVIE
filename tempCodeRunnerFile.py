import os
import whisper
from moviepy.editor import VideoFileClip, AudioFileClip
from deep_translator import GoogleTranslator
from gtts import gTTS

# ---- ĐƯỜNG DẪN ----
video_path = r"C:\Users\vuchi\Downloads\video.mp4"
audio_path = r"C:\Users\vuchi\OneDrive\Desktop\Python 10\HOA10\output.wav"
translated_audio_path = r"C:\Users\vuchi\Downloads\chemistry_vi.wav"
output_video_path = r"C:\Users\vuchi\Downloads\chemistry_vi.mp4"

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
tts = gTTS(full_text_vi, lang="vi")
tts.save(translated_audio_path)

# ---- 5. GHÉP LẠI VIDEO (tuỳ chọn) ----
print("🎬 Đang ghép lại video với tiếng Việt...")
new_audio = AudioFileClip(translated_audio_path)
final_video = video.set_audio(new_audio)
final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

print("✅ Xong! Có file WAV:", translated_audio_path)
print("✅ Và video kèm tiếng Việt:", output_video_path)
