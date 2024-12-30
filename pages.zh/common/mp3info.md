# mp3info

> MP3 文件的 ID3v1 标签的查看器/编辑器（不支持 ID3v2 标签）。
> 更多信息：<https://www.ibiblio.org/mp3info>。

- 显示特定 MP3 文件的所有 ID3v1 标签：

`mp3info {{path/to/file.mp3}}`

- 交互式编辑 ID3v1 标签：

`mp3info -i {{path/to/file.mp3}}`

- 为特定 MP3 文件设置 ID3v1 标签的值：

`mp3info -a "{{artist_name}}" -t "{{song_title}}" -l "{{album_title}}" -y {{year}} -c "{{comment_text}}" {{path/to/file.mp3}}`

- 为特定 MP3 文件设置专辑中的曲目编号：

`mp3info -n {{track_number}} {{path/to/file.mp3}}`

- 打印有效流派及其数字代码的列表：

`mp3info -G`

- 为特定 MP3 文件设置音乐流派：

`mp3info -g {{genre_number}} {{path/to/file.mp3}}`