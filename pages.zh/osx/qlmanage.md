# qlmanage

> QuickLook 服务器工具。
> 更多信息：<https://keith.github.io/xcode-man-pages/qlmanage.1.html>.

- 快速显示一个或多个文件：

`qlmanage -p {{路径/到/文件1 路径/到/文件2 ...}}`

- 计算生成当前目录中所有 jpeg 文件的缩略图，300px 宽 png 格式，并将它们放在一个指定目录中：

`qlmanage {{*.jpg}} -t -s {{300}} {{指定目录}}`

- 重置快速查看：

`qlmanage -r`
