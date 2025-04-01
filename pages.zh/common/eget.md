# eget

> 从 GitHub 安装预编译的二进制文件。
> 更多信息：<https://github.com/zyedidia/eget>.

- 从 GitHub 仓库下载当前系统的预编译二进制文件：

`eget {{zyedidia/micro}}`

- 从 URL 下载：

`eget {{https://go.dev/dl/go1.17.5.linux-amd64.tar.gz}}`

- 指定下载文件的存放位置：

`eget {{zyedidia/micro}} --to={{path/to/directory}}`

- 指定使用 Git 标签而不是最新版本：

`eget {{zyedidia/micro}} --tag={{v2.0.10}}`

- 安装最新预发布版本而不是最新稳定版本：

`eget {{zyedidia/micro}} --pre-release`

- 仅下载资源文件，不进行解压：

`eget {{zyedidia/micro}} --download-only`

- 只有在有新版本时才下载：

`eget {{zyedidia/micro}} --upgrade-only`