# dget

> 下载 Debian 包。
> 更多信息：<https://manned.org/dget.1>。

- 下载一个二进制包：

`dget {{package}}`

- 从其 `.dsc` 文件下载并提取一个包源：

`dget {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`

- 从其 `.dsc` 文件下载一个包源 tarball，但不提取它：

`dget -d {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`