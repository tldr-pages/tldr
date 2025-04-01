# gdebi

> 简单安装 `.deb` 文件。
> 更多信息：<https://www.commandlinux.com/man-page/man1/gdebi.1.html>.

- 安装本地 `.deb` 包，解析并安装其依赖项：

`gdebi {{path/to/package.deb}}`

- 不显示进度信息：

`gdebi {{path/to/package.deb}} --quiet`

- 设置 APT 配置选项：

`gdebi {{path/to/package.deb}} --option={{APT_OPTS}}`

- 使用替代的根目录：

`gdebi {{path/to/package.deb}} --root={{path/to/root_dir}}`

- 显示版本信息：

`gdebi --version`