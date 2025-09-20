First, if you want to run code. I must download some library on python =))), it very very very improtant because if not have this library, you DO NOT RUN CODE
I think you should use vscode (Visual Studio Code) to easy to do this project by my code :P
1. You need install python 3.13 on web or micrsoft store and setup in your PC, PLS remember tick into blank "Add Python to PATH".
2. Open terminal in VSCode and text. You can copy and paster each line "pip install git+https://github.com/openai/whisper.git"
3. "pip install deep-translator"
4. "pip install moviepy"
5. "pip install gtts"
However, that's still not enough. You must download ffmpeg to your PC to run code smooth and not error encountered
6. go to gg and paster this link "https://www.ffmpeg.org/download.html". Download this file and Extract All
7. In line 4 on audio.py file, at "...". Point to where you put the video file
8. In line 8 on project.py file, at "...". Delete ... and change this file ffmpeg you just extracted and point to the bin\ffmpeg.exe
9. In line 11 on project.py file, at "...". You need point to where you put the video file
10. In line 12 on project.py file, at "...". You need point to where you put the audio fie (.wav) when you save in step 7 (you can open explore to find)
11. In line 13 on project.py file, at "...". You must fill the location you want to save this audio after translate
Finish=)))
