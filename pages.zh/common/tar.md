# tar

> 存档工具。
> 通常与压缩方法结合使用，例如 `gzip` 或 `bzip2`。
> 更多信息：<https://www.gnu.org/software/tar>。

- [c] 创建一个存档并将其写入 [f] 文件：

`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}`

- [c] 创建一个 g[z] 压缩存档并将其写入 [f] 文件：

`tar czf {{path/to/target.tar.gz}} {{path/to/file1 path/to/file2 ...}}`

- [c] 从一个目录使用相对路径创建一个 g[z] 压缩（压缩）存档：

`tar czf {{path/to/target.tar.gz}} --directory={{path/to/directory}} .`

- E[x] 将一个（压缩的）存档 [f] 文件解压到当前目录，且详细显示：

`tar xvf {{path/to/source.tar[.gz|.bz2|.xz]}}`

- E[x] 将一个（压缩的）存档 [f] 文件解压到目标目录：

`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}} --directory={{path/to/directory}}`

- [c] 创建一个压缩存档并将其写入 [f] 文件，使用文件扩展名 [a] 自动确定压缩程序：

`tar caf {{path/to/target.tar.xz}} {{path/to/file1 path/to/file2 ...}}`

- Lis[t] 详细列出 tar [f] 文件的内容：

`tar tvf {{path/to/source.tar}}`

- E[x] 从存档 [f] 文件中提取匹配模式的文件：

`tar xf {{path/to/source.tar}} --wildcards "{{*.html}}"`