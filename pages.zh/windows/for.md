# 循环执行

> 有条件地多次执行命令。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/for>。

- 对指定的集合执行给定命令：

`for %{{变量}} in ({{项_a 项_b 项_c}}) do ({{echo 循环已执行}})`

- 遍历给定范围的数字：

`for /l %{{变量}} in ({{起始}}, {{步长}}, {{结束}}) do ({{echo 循环已执行}})`

- 遍历给定的文件列表：

`for %{{变量}} in ({{路径\to\文件1.ext 路径\to\文件2.ext ...}}) do ({{echo 循环已执行}})`

- 遍历给定的目录列表：

`for /d %{{变量}} in ({{路径\to\目录1.ext 路径\to\目录2.ext ...}}) do ({{echo 循环已执行}})`

- 在每个目录中执行给定命令：

`for /d %{{变量}} in (*) do (if exist %{{变量}} {{echo 循环已执行}})`