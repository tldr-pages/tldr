# youtube-dl

> Download videos from YouTube and other websites.
> More information: <http://rg3.github.io/youtube-dl/>.

- Download a video or playlist:

`youtube-dl {{https://www.youtube.com/watch?v=oHg5SJYRHA0}}`

- List all formats that a video or playlist is available in:

`youtube-dl --list-formats {{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}`

- Download a video or playlist at a specific quality:

`youtube-dl --format "{{best[height<=480]}}" {{https://www.youtube.com/watch?v=oHg5SJYRHA0}}`

- Download the audio from a video and convert it to an MP3:

`youtube-dl -x --audio-format {{mp3}} {{url}}`

- Download the best quality audio and video and merge them:

`youtube-dl -f bestvideo+bestaudio {{url}}`

- Download video(s) as MP4 files with custom filenames:

`youtube-dl --format {{mp4}} -o "{{%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" {{url}}`

- Download a particular language's subtitles along with the video:

`youtube-dl --sub-lang {{en}} --write-sub {{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}`

- Download a playlist and extract mp3 from it:

`youtube-dl -i --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" {{url to playlist}}`
