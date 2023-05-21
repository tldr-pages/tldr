# qlmanage

> QuickLook 服务器工具。
> 更多信息：<https://ss64.com/osx/qlmanage.html>.

- 快速显示一个或多个文件：

`qlmanage -p {{路径/到/文件1个 路径/到/文件2个 ...}}`

- 计算生成当前目录中所有 jpeg 文件的缩略图，300px 宽 png 格式，并将它们放在一个指定目录中：

`qlmanage {{*.jpg}} -t -s {{300}} {{指定目录}}`

- 重置快速查看：

`qlmanage -r`
