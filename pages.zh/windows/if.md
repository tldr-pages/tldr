# 如果

> 在批处理脚本中执行条件处理。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/if>。

- 如果条件为真，则执行指定的命令：

`if {{condition}} ({{echo 条件为真}})`

- 如果条件为假，则执行指定的命令：

`if not {{condition}} ({{echo 条件为真}})`

- 如果条件为真则执行第一个指定的命令，否则执行第二个指定的命令：

`if {{condition}} ({{echo 条件为真}}) else ({{echo 条件为假}})`

- 检查 `%errorlevel%` 是否大于或等于指定的退出代码：

`if errorlevel {{2}} ({{echo 条件为真}})`

- 检查两个字符串是否相等：

`if %{{variable}}% == {{string}} ({{echo 条件为真}})`

- 检查两个字符串是否相等且不区分大小写：

`if /i %{{variable}}% == {{string}} ({{echo 条件为真}})`

- 检查文件是否存在：

`if exist {{path\to\file}} ({{echo 条件为真}})`