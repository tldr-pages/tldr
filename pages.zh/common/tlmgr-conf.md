# tlmgr conf

> 管理 TeX Live 配置。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>.

- 显示当前的 TeX Live 配置：

`tlmgr conf`

- 显示当前的 `texmf`、`tlmgr` 或 `updmap` 配置：

`tlmgr conf {{texmf|tlmgr|updmap}}`

- 显示特定的配置选项：

`tlmgr conf {{texmf|tlmgr|updmap}} {{configuration_key}}`

- 设置特定的配置选项：

`tlmgr conf {{texmf|tlmgr|updmap}} {{configuration_key}} {{value}}`

- 删除特定的配置选项：

`tlmgr conf {{texmf|tlmgr|updmap}} --delete {{configuration_key}}`

- 禁用通过 `\write18` 执行系统调用：

`tlmgr conf texmf {{shell_escape}} {{0}}`

- 显示所有额外的 `texmf` 树：

`tlmgr conf auxtrees show`
