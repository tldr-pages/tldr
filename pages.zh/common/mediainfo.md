# mediainfo

> 显示视频和音频文件的元数据。
> 更多信息：<https://mediaarea.net/MediaInfo>。

- 在控制台中显示给定文件的元数据：

`mediainfo {{file}}`

- 将输出保存到指定文件的同时也在控制台显示：

`mediainfo --Logfile={{out.txt}} {{file}}`

- 列出可以提取的元数据属性：

`mediainfo --Info-Parameters`
