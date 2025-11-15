# fzf

> 命令行模糊查找器。
> 类似于 `sk`.
> 更多信息：<https://github.com/junegunn/fzf#usage>.

- 对指定目录中的所有文件启动 `fzf`:

`find {{路径/到/目录}} -type f | fzf`

- 为正在运行的进程启动 `fzf`:

`ps aux | fzf`

- 使用 `<Shift Tab>` 选择多个文件并将结果写入文件：

`find {{路径/到/目录}} -type f | fzf {{[-m|--multi]}} > {{路径/到/文件}}`

- 使用指定查询词启动 `fzf`:

`fzf {{[-q|--query]}} "{{查询词}}"`

- 对以 core 开头、以 go, rb 或 py 结尾的条目启动 `fzf`:

`fzf {{[-q|--query]}} "^core go$ | rb$ | py$"`

- 对不匹配 pyc 且完全匹配 travis 的条目启动 `fzf`:

`fzf {{[-q|--query]}} "!pyc 'travis"`
