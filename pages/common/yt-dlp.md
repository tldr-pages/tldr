# yt-dlp

> A youtube-dl fork with additional features and fixes.
> Download videos from YouTube and other websites.
> More information: <https://github.com/yt-dlp/yt-dlp>.

- Download a video or playlist (with the default options from command below):

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Download a video with a defined format, in this case the best mp4 video available (default is "bv\*+ba/b"):

`yt-dlp --format "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Extract audio from videos (required ffmpeg or ffprobe):

`yt-dlp --extract-audio "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Specify audio format of extracted audio (the default is "best"):

`yt-dlp --extract-audio --audio-format {{mp3}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Specify audio quality of extracted audio (between 0 (best) and 10 (worst), default = 5):

`yt-dlp --extract-audio --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Download all playlists of YouTube channel/user keeping each playlist in separate directory:

`yt-dlp -o "{{%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home:

`yt-dlp -u {{user}} -p {{password}} -P "{{~/MyVideos}}" -o "{{%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`

- Download entire series season keeping each series and each season in separate directory under C:/MyVideos:

`yt-dlp -P "{{C:/MyVideos}}" -o "{{%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s}}" "{{https://videomore.ru/kino_v_detalayah/5_sezon/367617}}"`
