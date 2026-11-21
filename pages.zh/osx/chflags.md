# chflags

> 更改文件或文件夹的标志。
> 更多信息：<https://keith.github.io/xcode-man-pages/chflags.1.html>。

- 给文件设置 hidden（隐藏）标签：

`chflags hidden {{路径/到/文件}}`

- 取消文件的 hidden 标签：

`chflags nohidden {{路径/到/文件}}`

- 递归地给文件夹中每个文件设置 uchg 标志：

`chflags -R uchg {{路径/到/目录}}`

- 递归地撤销文件夹中每个文件设置的 uchg 标志：

`chflags -R nouchg {{路径/到/目录}}`
