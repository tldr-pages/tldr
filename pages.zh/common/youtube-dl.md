# youtube-dl

> 从 YouTube 和其他网站下载视频。
> 请参阅：`yt-dlp`，`ytfzf`，`you-get`。
> 更多信息：<https://rg3.github.io/youtube-dl/>.

- 下载一个视频或播放列表：

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- 列出视频或播放列表的所有可用格式：

`youtube-dl --list-formats '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- 以特定质量下载视频或播放列表：

`youtube-dl --format "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- 下载视频的音频并将其转换为 MP3：

`youtube-dl -x --audio-format {{mp3}} '{{url}}'`

- 下载最佳质量的音频和视频并合并它们：

`youtube-dl -f bestvideo+bestaudio '{{url}}'`

- 将视频下载为 MP4 文件并自定义文件名：

`youtube-dl --format {{mp4}} -o "{{%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- 下载特定语言的字幕并与视频一起保存：

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- 下载一个播放列表并从中提取 MP3：

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" '{{url_to_playlist}}'`
