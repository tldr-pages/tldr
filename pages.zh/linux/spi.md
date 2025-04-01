# spi

> 一个元包管理器，处理包和 Slackbuilds。
> 更多信息：<https://github.com/gapan/spi>.

- 更新可用包和 Slackbuilds 的列表：

`spi --update`

- 安装包或 Slackbuild：

`spi --install {{package/slackbuild_name}}`

- 升级所有已安装的包到最新版本：

`spi --upgrade`

- 通过包名或描述查找包或 Slackbuilds：

`spi {{search_terms}}`

- 显示包或 Slackbuild 的信息：

`spi --show {{package/slackbuild_name}}`

- 清理本地包和 Slackbuild 缓存：

`spi --clean`