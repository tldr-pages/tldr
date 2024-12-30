# makepkg

> 创建一个可以与 `pacman` 一起使用的软件包。
> 默认使用当前工作目录中的 `PKGBUILD` 文件。
> 更多信息请访问：<https://manned.org/makepkg.8>。

- 创建一个软件包：

`makepkg`

- 创建一个软件包并安装其依赖：

`makepkg --syncdeps`

- 创建一个软件包，安装其依赖，然后将其安装到系统中：

`makepkg --syncdeps --install`

- 创建一个软件包，但跳过检查源的哈希值：

`makepkg --skipchecksums`

- 在成功构建后清理工作目录：

`makepkg --clean`

- 验证源的哈希值：

`makepkg --verifysource`

- 生成并保存源信息到 `.SRCINFO` 文件中：

`makepkg --printsrcinfo > .SRCINFO`