# pkgmk

> 为 CRUX 中使用 pkgadd 生成二进制包。
> 更多信息：<https://docs.oracle.com/cd/E88353_01/html/E37839/pkgmk-1.html>.

- 创建并下载包：

`pkgmk -d`

- 创建包后安装包：

`pkgmk -d -i`

- 创建包后升级包：

`pkgmk -d -u`

- 创建包时忽略足迹：

`pkgmk -d -if`

- 创建包时忽略 MD5 校验和：

`pkgmk -d -im`

- 更新包的足迹：

`pkgmk -uf`