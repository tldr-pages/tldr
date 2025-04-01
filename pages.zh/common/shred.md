# shred

> 覆盖文件内容以安全删除数据。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html>.

- 覆盖文件内容：

`shred {{path/to/file}}`

- 覆盖文件内容，并在屏幕上显示进度：

`shred {{[-v|--verbose]}} {{path/to/file}}`

- 覆盖文件内容，使用零而不是随机数据：

`shred {{[-z|--zero]}} {{path/to/file}}`

- 覆盖文件指定次数：

`shred {{[-n|--iterations]}} {{25}} {{path/to/file}}`

- 覆盖并删除文件：

`shred --remove {{path/to/file}}`

- 覆盖文件100次，最后用零覆盖一次，覆盖后删除文件，并在屏幕上显示详细进度：

`shred {{[-vzun|--verbose --zero -u --iterations]}} 100 {{path/to/file}}`
