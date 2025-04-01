# expect

> 用于与需要用户输入的其他程序交互的脚本执行器。
> 更多信息：<https://manned.org/expect>.

- 从文件中执行 expect 脚本：

`expect {{path/to/file}}`

- 执行指定的 expect 脚本：

`expect -c "{{commands}}"`

- 进入交互式 REPL（使用 `exit` 或 `<Ctrl d>` 退出）：

`expect -i`