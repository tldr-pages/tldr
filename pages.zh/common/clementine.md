# clementine

> 一个现代音乐播放器和音乐库管理器。
> 参见: `audacious`, `qmmp`, `cmus`, `mpv`。
> 更多信息: <https://github.com/clementine-player/Clementine/wiki>。

- 启动图形界面或将其置于前端：

`clementine`

- 开始播放音乐：

`clementine {{url|path/to/music.ext}}`

- 切换暂停和播放状态：

`clementine --play-pause`

- 停止播放：

`clementine --stop`

- 跳到下一首或上一首曲目：

`clementine --{{next|previous}}`

- 使用一个或多个音乐文件或URL创建新播放列表：

`clementine --create {{url1 url2 ... | path/to/music1.ext path/to/music2.ext ...}}`

- 加载播放列表文件：

`clementine --load {{path/to/playlist.ext}}`

- 播放当前加载的播放列表中的特定曲目：

`clementine --play-track {{5}}`
