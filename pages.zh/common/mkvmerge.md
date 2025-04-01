# mkvmerge

> 合并和提取多媒体流。
> 更多信息：<https://mkvtoolnix.download/doc/mkvmerge.html>。

- 显示有关 Matroska 文件的信息：

`mkvmerge --identify {{path/to/file.mkv}}`

- 从指定文件的第 1 轨道提取音频：

`mkvextract tracks {{path/to/file.mkv}} {{1}}:{{path/to/output.webm}}`

- 从指定文件的第 3 轨道提取字幕：

`mkvextract tracks {{path/to/file.mkv}} {{3}}:{{path/to/subs.srt}}`

- 向文件中添加字幕轨道：

`mkvmerge --output {{path/to/output.mkv}} {{path/to/file.mkv}} {{path/to/subs.srt}}`