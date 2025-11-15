# yt-dlp

> 一个具有额外功能和修复的 youtube-dl 分支。
> 从 YouTube 和其他网站下载视频。
> 请参阅：`yt-dlp`，`ytfzf`。
> 更多信息：<https://github.com/yt-dlp/yt-dlp#usage-and-options>.

- 下载视频或播放列表（使用下面命令的默认选项）：

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- 列出可下载的视频格式：

`yt-dlp --list-formats "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- 使用最佳 MP4 视频格式下载视频或播放列表（默认为 "bv\*+ba/b"）：

`yt-dlp --format "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- 从视频中提取音频（需要 ffmpeg 或 ffprobe）：

`yt-dlp --extract-audio "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- 指定提取音频的格式和音质（0（最佳）到 10（最差），默认值为 5）：

`yt-dlp --extract-audio --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- 仅下载播放列表中的第二、第四、第五、第六和最后一项（第一项为 1，而非 0）：

`yt-dlp --playlist-items 2,4:6,-1 "{{https://youtube.com/playlist?list=PLbzoR-pLrL6pTJfLQ3UwtB-3V4fimdqnA}}"`

- 下载 YouTube 频道/用户的所有播放列表，并将每个播放列表保存在单独的目录中：

`yt-dlp -o "{{%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- 下载 Udemy 课程，并将每章保存在单独的目录中：

`yt-dlp -u {{用户}} -p {{密码}} -P "{{路径/到/目录}}" -o "{{%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`
