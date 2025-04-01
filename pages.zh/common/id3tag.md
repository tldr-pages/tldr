# id3tag

> 读取、写入和操作 MP3 文件的 ID3v1 和 ID3v2 标签。
> 更多信息：<https://manned.org/id3tag>.

- 设置 MP3 文件的艺术家和歌曲标题标签：

`id3tag --artist {{artist}} --song {{song_title}} {{path/to/file.mp3}}`

- 设置当前目录中所有 MP3 文件的专辑标题：

`id3tag --album {{album}} {{*.mp3}}`

- 显示帮助：

`id3tag --help`
