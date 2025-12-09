# yadm gitconfig

> 向 `git config` 传递选项。更改由 `yadm` 管理的仓库的 `.gitconfig`。
> 请参阅：`git config`。
> 更多信息：<https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#commands>.

- 更新或设置一个 Git 配置值：

`yadm gitconfig {{键.内键}} {{值}}`

- 从 `yadm` 的 Git 配置中获取一个值：

`yadm gitconfig --get {{键}}`

- 在 `yadm` 的 Git 配置中取消设置一个值：

`yadm gitconfig --unset {{键}}`

- 列出 `yadm` 的 Git 配置中的所有值：

`yadm gitconfig --list`
