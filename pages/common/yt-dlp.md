# yt-dlp

> A youtube-dl fork with additional features and fixes.
> Download videos from YouTube and other websites.
> See also: `yt-dlp`, `ytfzf`.
> More information: <https://github.com/yt-dlp/yt-dlp>.

- Download a video or playlist (with the default options from command below):

`yt-dlp "{{url}}"`

- List all formats that a video or playlist is available in:

`yt-dlp --list-formats "{{url}}"`

- Download a video or playlist at a specific quality:

`yt-dlp --format "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{url}}"`

- Extract audio from a video (requires ffmpeg or ffprobe):

`yt-dlp --extract-audio "{{url}}"`

- Specify audio format and audio quality of extracted audio (between 0 (best) and 10 (worst), default = 5):

`yt-dlp --extract-audio --audio-format {{mp3}} --audio-quality {{0}} "{{url}}"`

- Download all playlists of YouTube channel/user keeping each playlist in separate directory:

`yt-dlp -o "{{%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s}}" "{{url}}"`

- Download Udemy course keeping each chapter in separate directory under path/to/directory directory in your home:

`yt-dlp -u {{user}} -p {{password}} -P "{{path/to/directory}}" -o "{{%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s}}" "{{url}}"`

- Download entire series season keeping each series and each season in separate directory under path/to/directory:

`yt-dlp -P "{{path/to/directory}}" -o "{{%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s}}" "{{url}}"`
