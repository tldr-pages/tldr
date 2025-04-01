# mid3v2

> 编辑音频标签。
> 参见：`id3v2`。
> 更多信息：<https://mutagen.readthedocs.io/en/latest/man/mid3v2.html>.

- 列出所有受支持的 ID3v2.3 或 ID3v2.4 帧及其含义：

`id3v2 --list-frames {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- 列出所有受支持的 ID3v1 数字流派：

`id3v2 --list-genres {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- 列出特定文件中的所有标签：

`id3v2 --list {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- 设置特定的艺术家、专辑或歌曲信息：

`id3v2 {{--artist|--album|--song}}={{string}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- 设置特定的图片信息：

`id3v2 --picture={{filename:description:image_type:mime_type}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- 设置特定的年份信息：

`id3v2 --year={{YYYY}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- 设置特定的日期信息：

`id3v2 --date={{YYYY-MM-DD}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`