# dget

> 下载 Debian 软件包。
> 更多信息：<https://manned.org/dget.1>.

- 下载二进制软件包：

`dget {{package}}`

- 从 `.dsc` 文件下载并解压软件包源码：

`dget {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`

- 从 `.dsc` 文件下载软件包源码压缩包但不解压：

`dget -d {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`
