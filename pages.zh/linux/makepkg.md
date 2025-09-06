# makepkg

> 创建 `pacman` 可用的软件包。
> 默认使用当前工作目录中的 `PKGBUILD` 文件。
> 更多信息：<https://manned.org/makepkg.8>.

- 构建软件包：

`makepkg`

- 构建软件包并使用 `pacman` 安装缺失的依赖关系：

`makepkg {{[-s|--syncdeps]}}`

- 构建软件包、安装缺失的依赖后将其安装到系统：

`makepkg {{[-s|--syncdeps]}} {{[-i|--install]}}`

- 构建软件包但不验证源文件的检验值：

`makepkg --skipchecksums`

- 编译后清理工作文件：

`makepkg {{[-c|--clean]}}`

- 下载源文件（如果不存在）并进行完整性检查：

`makepkg --verifysource`

- 生成 `SRCINFO` 并写入到 `.SRCINFO` 文件：

`makepkg --printsrcinfo > .SRCINFO`
