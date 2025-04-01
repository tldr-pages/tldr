# for

> 条件性地多次执行命令。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/for>.

- 在指定集合上执行给定命令：

`for %{{variable}} in ({{item_a item_b item_c}}) do ({{echo 循环被执行}})`

- 在给定的数字范围内迭代：

`for /l %{{variable}} in ({{from}}, {{step}}, {{to}}) do ({{echo 循环被执行}})`

- 在给定的文件列表中迭代：

`for %{{variable}} in ({{path\to\file1.ext path\to\file2.ext ...}}) do ({{echo 循环被执行}})`

- 在给定的目录列表中迭代：

`for /d %{{variable}} in ({{path\to\directory1.ext path\to\directory2.ext ...}}) do ({{echo 循环被执行}})`

- 在每个目录中执行给定命令：

`for /d %{{variable}} in (*) do (if exist %{{variable}} {{echo 循环被执行}})`