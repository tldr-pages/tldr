# touch

> 创建文件并设置访问/修改时间。
> 更多信息：<https://manned.org/touch>。

- 创建特定文件：

`touch {{path/to/file1 path/to/file2 ...}}`

- 将文件的 [a]ccess 或 [m]odification 时间设置为当前时间，如果文件不存在则不 [c]reate 文件：

`touch -c -{{a|m}} {{path/to/file1 path/to/file2 ...}}`

- 将文件 [t]ime 设置为特定值，如果文件不存在则不 [c]reate 文件：

`touch -c -t {{YYYYMMDDHHMM.SS}} {{path/to/file1 path/to/file2 ...}}`

- 将文件的时间戳设置为 [r]eference 文件的时间戳，如果文件不存在则不 [c]reate 文件：

`touch -c -r {{path/to/reference_file}} {{path/to/file1 path/to/file2 ...}}`