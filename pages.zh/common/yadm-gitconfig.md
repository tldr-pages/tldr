# yadm-gitconfig

> 将选项传递给 `git config`。更改由 `yadm` 管理的仓库的 `.gitconfig`。
> 另请参见：`git config`。
> 更多信息：<https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#commands>。

- 更新或设置 Git 配置值：

`yadm gitconfig {{key.inner-key}} {{value}}`

- 从 `yadm` 的 Git 配置中获取值：

`yadm gitconfig --get {{key}}`

- 在 `yadm` 的 Git 配置中取消设置值：

`yadm gitconfig --unset {{key}}`

- 列出 `yadm` 的 Git 配置中的所有值：

`yadm gitconfig --list`