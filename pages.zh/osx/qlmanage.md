# qlmanage

> QuickLook服务器工具.

- 快速显示一个或多个文件:

`qlmanage -p {{文件名}} {{文件名2}}`

- 计算生成当前目录中所有 jpeg 文件的缩略图, 300px宽 png格式,并将它们放在一个指定目录中:
`qlmanage {{*.jpg}} -t -s {{300}} {{指定目录}}`

- 重置快速查看:

`qlmanage -r`
