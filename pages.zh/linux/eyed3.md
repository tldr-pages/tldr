# eyeD3

> 读取和操作 MP3 文件的元数据。
> 更多信息：<https://eyed3.readthedocs.io>.

- 查看 MP3 文件的信息：

`eyeD3 {{filename.mp3}}`

- 设置 MP3 文件的标题：

`eyeD3 --title "{{A Title}}" {{filename.mp3}}`

- 设置目录中所有 MP3 文件的专辑名称：

`eyeD3 --album "{{Album Name}}" {{*.mp3}}`

- 为 MP3 文件设置封面图片：

`eyeD3 --add-image {{front_cover.jpeg}}:FRONT_COVER: {{filename.mp3}}`
