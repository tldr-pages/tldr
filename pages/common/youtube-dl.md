# youtube-dl

> Download videos from YouTube and other websites.

- Download a video or playlist:

`youtube-dl {{https://www.youtube.com/watch?v=oHg5SJYRHA0}}`

- Download the audio from a video and convert it to an MP3:

`youtube-dl -x --audio-format {{mp3}} {{url}}`

- Download video(s) as MP4 files with custom filenames:

`youtube-dl --format {{mp4}} --output {{"%(title) by %(uploader) on %(upload_date) in %(playlist).%(ext)"}} {{url}}`

- Download a video and save its description, metadata, annotations, subtitles, and thumbnail:

`youtube-dl --write-description --write-info-json --write-annotations --write-sub --write-thumbnail {{url}}`

- From a playlist, download all "Let's Play" videos that aren't marked "NSFW" or age-restricted for 7 year-olds:

`youtube-dl --match-title {{"let's play"}} --age-limit {{7}} --reject-title {{"nsfw"}} {{playlist_url}}`
