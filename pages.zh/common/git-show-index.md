# git show-index

> 显示 Git 仓库的打包归档索引。
> 更多信息：<https://git-scm.com/docs/git-show-index>。

- 读取 Git 打包文件的 IDX 文件并将其内容输出到 `stdout`：

`git show-index {{path/to/file.idx}}`

- 指定索引文件的哈希算法（实验性功能）：

`git show-index --object-format={{sha1|sha256}} {{path/to/file}}`
