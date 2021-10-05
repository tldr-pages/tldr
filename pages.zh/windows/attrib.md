# attrib

> 显示或修改文件和目录的属性。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/attrib>.

- 显示当前目录下所有文件的属性：

`attrib`

- 显示当前目录和其子目录下所有文件的属性：

`attrib /S`

- 显示当前目录和其子目录下所有文件和目录的属性：

`attrib /S /D`

- 为一个文件增加只读属性：

`attrib +R {{document.txt}}`

- 删除一个文件的系统和隐藏属性：

`attrib -S -H {{document.txt}}`

- 为一个目录增加隐藏属性：

`attrib +H {{目录的路径}}`
