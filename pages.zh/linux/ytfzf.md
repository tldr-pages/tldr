# ytfzf

> 查找并下载视频和音乐。使用POSIX shell编写。
> 另请参见：`youtube-dl`，`yt-dlp`，`instaloader`。
> 更多信息：<https://github.com/pystardust/ytfzf>。

- 在YouTube上搜索视频并显示缩略图预览：

`ytfzf --show-thumbnails {{search_pattern}}`

- 循环播放第一个项目的音频：

`ytfzf --audio-only --auto-select --loop {{search_pattern}}`

- 从历史记录中下载视频：

`ytfzf --download --choose-from-history`

- 播放搜索中找到的所有音乐：

`ytfzf --audio-only --select-all {{search_pattern}}`

- 在外部菜单中查看热门视频：

`ytfzf --trending --ext-menu {{search_pattern}}`

- 在PeerTube上搜索而不是YouTube：

`ytfzf --peertube {{search_pattern}}`