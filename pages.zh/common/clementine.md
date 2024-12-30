# clementine

> 一个现代音乐播放器和库组织工具。
> 另见：`audacious`，`qmmp`，`cmus`，`mpv`。
> 更多信息：<https://github.com/clementine-player/Clementine/wiki>。

- 启动GUI或将其置于前台：

`clementine`

- 开始播放音乐：

`clementine {{url|path/to/music.ext}}`

- 切换暂停和播放状态：

`clementine --play-pause`

- 停止播放：

`clementine --stop`

- 跳到下一首或上一首曲目：

`clementine --{{next|previous}}`

- 创建一个包含一个或多个音乐文件或网址的新播放列表：

`clementine --create {{url1 url2 ... | path/to/music1.ext path/to/music2.ext ...}}`

- 加载一个播放列表文件：

`clementine --load {{path/to/playlist.ext}}`

- 在当前加载的播放列表中播放特定曲目：

`clementine --play-track {{5}}`