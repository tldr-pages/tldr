# lz4

> 压缩或解压缩 .lz4 文件。
> 更多信息：<https://github.com/lz4/lz4>.

- 压缩文件：

`lz4 {{path/to/file}}`

- 解压缩文件：

`lz4 -d {{file.lz4}}`

- 解压缩文件并写入 `stdout`：

`lz4 -dc {{file.lz4}}`

- 打包并压缩目录及其内容：

`tar cvf - {{path/to/directory}} | lz4 - {{dir.tar.lz4}}`

- 解压缩并解包目录及其内容：

`lz4 -dc {{dir.tar.lz4}} | tar -xv`

- 使用最佳压缩比压缩文件：

`lz4 -9 {{path/to/file}}`