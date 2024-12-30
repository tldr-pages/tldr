# findstr

> 在一个或多个文件中查找指定文本。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/findstr>。

- 在所有文件中查找一个或多个字符串：

`findstr "{{string1 string2 ...}}" *`

- 在管道命令的输出中查找一个或多个字符串：

`{{dir}} | findstr "{{string1 string2 ...}}"`

- 在所有文件中递归查找一个或多个字符串：

`findstr /s "{{string1 string2 ...}}" *`

- 使用不区分大小写的搜索查找字符串：

`findstr /i "{{string1 string2 ...}}" *`

- 在所有文件中使用正则表达式查找字符串：

`findstr /r "{{expression}}" *`

- 在所有文本文件中查找包含空格的字面字符串：

`findstr /c:"{{string1 string2 ...}}" *.txt`

- 在每个匹配行之前显示行号：

`findstr /n "{{string1 string2 ...}}" *`

- 仅显示包含匹配项的文件名：

`findstr /m "{{string1 string2 ...}}" *`