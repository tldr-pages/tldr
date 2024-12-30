# gdrive

> 与 Google Drive 互动。
> 文件夹/文件 ID 可以从 Google Drive 文件夹或 ID URL 获取。
> 更多信息：<https://github.com/gdrive-org/gdrive>。

- 将本地路径上传到指定 ID 的父文件夹：

`gdrive upload -p {{id}} {{path/to/file_or_folder}}`

- 根据 ID 将文件或目录下载到当前目录：

`gdrive download {{id}}`

- 根据 ID 下载到指定的本地路径：

`gdrive download --path {{path/to/folder}} {{id}}`

- 使用给定的文件或文件夹创建 ID 的新版本：

`gdrive update {{id}} {{path/to/file_or_folder}}`