from moviepy import VideoFileClip

# Đường dẫn tới video gốc
video_path = r"..."   # đổi thành tên file video của bạn
output_audio = "output.wav"

# Mở video
clip = VideoFileClip(video_path)

# Xuất audio sang file WAV
clip.audio.write_audiofile(output_audio, codec='pcm_s16le')

print(f"Đã xuất audio ra: {output_audio}")
