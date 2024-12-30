# debuild

> 从源代码构建 Debian 包。
> 更多信息：<https://manned.org/debuild.1>。

- 在当前目录中构建包：

`debuild`

- 仅构建二进制包：

`debuild -b`

- 构建包后不运行 lintian：

`debuild --no-lintian`