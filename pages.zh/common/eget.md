# eget

> 轻松从 GitHub 安装预构建的二进制文件。
> 更多信息：<https://github.com/zyedidia/eget>。

- 从 GitHub 上的一个仓库下载当前系统的预构建二进制文件：

`eget {{zyedidia/micro}}`

- 从 URL 下载：

`eget {{https://go.dev/dl/go1.17.5.linux-amd64.tar.gz}}`

- 指定下载文件的存放位置：

`eget {{zyedidia/micro}} --to={{path/to/directory}}`

- 指定 Git 标签，而不是使用最新版本：

`eget {{zyedidia/micro}} --tag={{v2.0.10}}`

- 安装最新的预发布版本，而不是最新的稳定版本：

`eget {{zyedidia/micro}} --pre-release`

- 仅下载资产，跳过解压：

`eget {{zyedidia/micro}} --download-only`

- 仅在有更新版本时下载，而不是当前已下载的版本：

`eget {{zyedidia/micro}} --upgrade-only`