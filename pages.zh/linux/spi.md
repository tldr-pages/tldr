# spi

> 一个处理软件包和Slackbuild的元包管理器。
> 更多信息请访问：<https://github.com/gapan/spi>。

- 更新可用软件包和Slackbuild的列表：

`spi --update`

- 安装软件包或Slackbuild：

`spi --install {{package/slackbuild_name}}`

- 升级所有已安装的软件包到最新版本：

`spi --upgrade`

- 通过软件包名称或描述查找软件包或Slackbuild：

`spi {{search_terms}}`

- 显示有关软件包或Slackbuild的信息：

`spi --show {{package/slackbuild_name}}`

- 清除本地软件包和Slackbuild缓存：

`spi --clean`