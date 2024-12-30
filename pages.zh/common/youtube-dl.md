# youtube-dl

> 从YouTube和其他网站下载视频。
> 另见：`yt-dlp`，`ytfzf`，`you-get`。
> 更多信息：<https://rg3.github.io/youtube-dl/>.

- 下载视频或播放列表：

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- 列出视频或播放列表可用的所有格式：

`youtube-dl --list-formats '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- 以特定质量下载视频或播放列表：

`youtube-dl --format "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- 下载视频的音频并转换为MP3：

`youtube-dl -x --audio-format {{mp3}} '{{url}}'`

- 下载最佳质量的音频和视频并合并：

`youtube-dl -f bestvideo+bestaudio '{{url}}'`

- 将视频下载为MP4文件并自定义文件名：

`youtube-dl --format {{mp4}} -o "{{%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- 下载特定语言的字幕并与视频一起下载：

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- 下载播放列表并从中提取MP3：

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" '{{url_to_playlist}}'`