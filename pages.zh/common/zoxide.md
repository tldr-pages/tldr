# zoxide

> 记录最常使用的目录。
> 使用一个排序算法来导航到最佳匹配。
> 更多信息：<https://github.com/ajeetdsouza/zoxide>.

- 转到名称中包含 "foo" 的排名最高的目录：

`zoxide query {{foo}}`

- 转到名称中依次包含 "foo" 和 "bar" 的排名最高的目录：

`zoxide query {{foo}} {{bar}}`

- 启动一个交互式目录搜索（需要 `fzf`）：

`zoxide query --interactive`

- 添加一个目录或提升其排名：

`zoxide add {{路径/到/目录}}`

- 从 `zoxide` 的数据库中移除一个目录：

`zoxide remove {{路径/到/目录}}`

- 为命令别名生成 shell 配置（`z`, `za`, `zi`, `zq`, `zr`）：

`zoxide init {{bash|fish|zsh}}`
