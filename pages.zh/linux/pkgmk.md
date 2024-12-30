# pkgmk

> 制作一个可在 CRUX 上使用 pkgadd 的二进制包。
> 更多信息：<https://docs.oracle.com/cd/E88353_01/html/E37839/pkgmk-1.html>。

- 制作并下载一个包：

`pkgmk -d`

- 制作后安装包：

`pkgmk -d -i`

- 制作后升级包：

`pkgmk -d -u`

- 制作包时忽略足迹：

`pkgmk -d -if`

- 制作包时忽略 MD5 校验和：

`pkgmk -d -im`

- 更新包的足迹：

`pkgmk -uf`