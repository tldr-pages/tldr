# mp3info

> MP3 文件的 ID3v1（而非 ID3v2）标签查看器/编辑器。
> 更多信息：<https://www.ibiblio.org/mp3info>.

- 显示特定 MP3 文件的所有 ID3v1 标签：

`mp3info {{path/to/file.mp3}}`

- 交互式编辑 ID3v1 标签：

`mp3info -i {{path/to/file.mp3}}`

- 设置特定 MP3 文件的 ID3v1 标签值：

`mp3info -a "{{artist_name}}" -t "{{song_title}}" -l "{{album_title}}" -y {{year}} -c "{{comment_text}}" {{path/to/file.mp3}}`

- 设置特定 MP3 文件在专辑中的曲目编号：

`mp3info -n {{track_number}} {{path/to/file.mp3}}`

- 打印有效流派及其数字代码的列表：

`mp3info -G`

- 设置特定 MP3 文件的音乐流派：

`mp3info -g {{genre_number}} {{path/to/file.mp3}}`