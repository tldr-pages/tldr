# createrepo

> 在目录中初始化一个 RPM 仓库，包括所有的 XML 和 SQLite 文件。
> 更多信息：<https://manned.org/createrepo>.

- 在目录中初始化一个基本的仓库：

`createrepo {{path/to/directory}}`

- 初始化一个仓库，排除测试 RPM 包并显示详细日志：

`createrepo -v -x {{test_*.rpm}} {{path/to/directory}}`

- 初始化一个仓库，使用 SHA1 作为校验和算法，并忽略符号链接：

`createrepo -S -s {{sha1}} {{path/to/directory}}`