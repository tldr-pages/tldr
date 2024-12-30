# asar

> 一个用于 Electron 平台的文件归档工具。
> 更多信息：<https://github.com/electron/asar>。

- 归档一个文件或目录：

`asar pack {{path/to/input_file_or_directory}} {{path/to/output_archive.asar}}`

- 解压一个归档：

`asar extract {{path/to/archive.asar}}`

- 从归档中提取特定文件：

`asar extract-file {{path/to/archive.asar}} {{file}}`

- 列出归档文件的内容：

`asar list {{path/to/archive.asar}}`