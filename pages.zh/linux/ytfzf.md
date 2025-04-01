# ytfzf

> 查找并下载视频和音乐。使用 POSIX shell 编写。
> 参见：`youtube-dl`，`yt-dlp`，`instaloader`。
> 更多信息：<https://github.com/pystardust/ytfzf>。

- 在 YouTube 上搜索带有缩略图预览的视频：

`ytfzf --show-thumbnails {{search_pattern}}`

- 仅播放搜索结果中第一个项目的音频并循环播放：

`ytfzf --audio-only --auto-select --loop {{search_pattern}}`

- 从历史记录中下载一个视频：

`ytfzf --download --choose-from-history`

- 播放搜索结果中找到的所有音乐：

`ytfzf --audio-only --select-all {{search_pattern}}`

- 在外部菜单中查看趋势视频：

`ytfzf --trending --ext-menu {{search_pattern}}`

- 在 PeerTube 上搜索而非 YouTube：

`ytfzf --peertube {{search_pattern}}`