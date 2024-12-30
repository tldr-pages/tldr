# zoxide

> 跟踪最常用的目录。
> 使用排名算法导航到最佳匹配。
> 更多信息：<https://github.com/ajeetdsouza/zoxide>。

- 转到名称中包含 "foo" 的最高排名目录：

`zoxide query {{foo}}`

- 转到名称中同时包含 "foo" 和 "bar" 的最高排名目录：

`zoxide query {{foo}} {{bar}}`

- 开始一个交互式目录搜索（需要 `fzf`）：

`zoxide query --interactive`

- 添加一个目录或增加其排名：

`zoxide add {{path/to/directory}}`

- 交互式地从 `zoxide` 的数据库中移除一个目录：

`zoxide remove {{path/to/directory}} --interactive`

- 为命令别名生成 shell 配置（`z`, `za`, `zi`, `zq`, `zr`）：

`zoxide init {{bash|fish|zsh}}`