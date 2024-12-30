# shred

> 通过覆盖文件安全删除数据。
> 更多信息：<https://www.gnu.org/software/coreutils/shred>。

- 覆盖一个文件：

`shred {{path/to/file}}`

- 覆盖一个文件并在屏幕上显示进度：

`shred --verbose {{path/to/file}}`

- 覆盖一个文件，用零代替随机数据：

`shred --zero {{path/to/file}}`

- 指定覆盖次数 [n]：

`shred --iterations {{25}} {{path/to/file}}`

- 覆盖一个文件并删除它：

`shred --remove {{path/to/file}}`

- 覆盖一个文件 100 次，最后用零进行一次覆盖，覆盖后删除文件，并在屏幕上显示详细进度：

`shred -vzun 100 {{path/to/file}}`