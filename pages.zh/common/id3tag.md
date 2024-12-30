# id3tag

> 读取、写入和操作MP3文件的ID3v1和ID3v2标签。
> 更多信息：<https://manned.org/id3tag>。

- 设置MP3文件的艺术家和歌曲标题标签：

`id3tag --artist {{artist}} --song {{song_title}} {{path/to/file.mp3}}`

- 设置当前目录中所有MP3文件的专辑标题：

`id3tag --album {{album}} {{*.mp3}}`

- 显示帮助信息：

`id3tag --help`