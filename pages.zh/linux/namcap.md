# namcap

> 检查二进制包和源 `PKGBUILD` 文件中的常见打包错误。
> 更多信息：<https://manned.org/namcap>.

- 检查特定的 `PKGBUILD` 文件：

`namcap {{path/to/pkgbuild}}`

- 检查特定的包文件：

`namcap {{path/to/package.pkg.tar.zst}}`

- 检查文件，并打印额外的信息性消息：

`namcap {{[-i|--info]}} {{path/to/file}}`