# shar

> 创建 shell 归档文件。
> 更多信息：<https://www.gnu.org/software/sharutils/manual/sharutils.html>.

- 创建一个 shell 脚本，执行时可以从脚本自身中提取指定的文件：

`shar {{[-V|--vanilla-operation]}} {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- 压缩归档文件中的文件：

`shar {{[-C|--compactor]}} {{xz}} {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- 将所有文件视为二进制文件（即使用 `uuencode` 编码所有文件）：

`shar {{[-B|--uuencode]}} {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- 将所有文件视为文本文件（即不使用 `uuencode` 编码任何文件）：

`shar {{[-T|--text-files]}} {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- 在归档文件的头注释中包含名称和分隔符：

`shar {{[-n|--archive-name]}} "{{My files}}" {{[-c|--cut-mark]}} {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`
