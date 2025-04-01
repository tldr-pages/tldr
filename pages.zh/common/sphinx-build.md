# sphinx-build

> Sphinx 文档生成器。
> 更多信息：<https://www.sphinx-doc.org/en/master/man/sphinx-build.html>.

- 构建文档：

`sphinx-build -b {{html|epub|text|latex|man|...}} {{源目录路径}} {{构建目录路径}}`

- 构建用于 readthedocs.io 的文档（需要安装 sphinx-rtd-theme pip 包）：

`sphinx-build -b {{html}} {{文档目录路径}} {{构建目录路径}}`