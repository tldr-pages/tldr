# truncate

> 缩小或扩展文件到指定大小。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html>.

- 将现有文件设置为 10 GB，或创建一个指定大小的新文件：

`truncate {{[-s|--size]}} 10G {{path/to/file}}`

- 将文件扩充 50 MiB，用空洞填充（读取时为零字节）：

`truncate {{[-s|--size]}} +50M {{path/to/file}}`

- 将文件缩小 2 GiB，通过从文件末尾删除数据实现：

`truncate {{[-s|--size]}} -2G {{path/to/file}}`

- 清空文件内容：

`truncate {{[-s|--size]}} 0 {{path/to/file}}`

- 清空文件内容，但如果文件不存在则不创建文件：

`truncate {{[-c|--no-create]}} {{[-s|--size]}} 0 {{path/to/file}}`