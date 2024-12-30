# git mergetool

> 运行合并冲突解决工具以解决合并冲突。
> 更多信息：<https://git-scm.com/docs/git-mergetool>。

- 启动默认的合并工具以解决冲突：

`git mergetool`

- 列出有效的合并工具：

`git mergetool --tool-help`

- 启动由名称识别的合并工具：

`git mergetool --tool {{tool_name}}`

- 在每次调用合并工具之前不提示：

`git mergetool --no-prompt`

- 显式使用 GUI 合并工具（请参见 `merge.guitool` 配置变量）：

`git mergetool --gui`

- 显式使用常规合并工具（请参见 `merge.tool` 配置变量）：

`git mergetool --no-gui`