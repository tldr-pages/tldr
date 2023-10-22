# findstr

> 在一个或多个文件中查找指定的文本。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/findstr>.

- 在所有文件中查找以空格分隔的字符串：

`findstr "{{查询语句 查询语句 ..}}" *`

- 以递归方式在所有文件中查找以空格分隔的字符串：

`findstr /s "{{查询语句 查询语句 ..}}" *`

- 查找时不区分大小写：

`findstr /i "{{查询语句}}" *"`

- 使用正则表达式搜索：

`findstr /r "{{正则表达式}}" *`

- 在所有文本文件中查找文字字符串（包含空格）：

`findstr /c:"{{查询语句}}" *.txt`

- 只查找完全匹配的行：

`findstr /x "{{查询语句}}" *`

- 显示匹配的行的行数：

`findstr /n "{{查询语句}}" *`

- 只显示匹配的文件名：

`findstr /m "{{查询语句}}" *`
