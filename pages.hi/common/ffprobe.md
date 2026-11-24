# ffprobe

> मल्टीमीडिया स्ट्रीम विश्लेषक।
> अधिक जानकारी: <https://ffmpeg.org/ffprobe.html>।

- मीडिया फ़ाइल की स्ट्रीम से जुड़ी सभी उपलब्ध जानकारी दिखाएं:

`ffprobe {{[-v|-loglevel]}} error -show_streams {{इनपुट.mp4}}`

- मीडिया की अवधि दिखाएं:

`ffprobe {{[-v|-loglevel]}} error -show_entries format=duration {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{इनपुट.mp4}}`

- वीडियो की फ़्रेम दर दिखाएं:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=avg_frame_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{इनपुट.mp4}}`

- वीडियो की चौड़ाई या ऊंचाई दिखाएं:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream={{width|height}} {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{इनपुट.mp4}}`

- वीडियो की औसत बिट दर दिखाएं:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=bit_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{इनपुट.mp4}}`
