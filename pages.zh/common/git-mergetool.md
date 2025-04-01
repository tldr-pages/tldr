# git mergetool

> 运行合并冲突解决工具以解决合并冲突。
> 更多信息：<https://git-scm.com/docs/git-mergetool>。

- 启动默认的合并工具以解决冲突：

`git mergetool`

- 列出有效的合并工具：

`git mergetool --tool-help`

- 启动由名称标识的合并工具：

`git mergetool --tool {{tool_name}}`

- 在每次调用合并工具之前不提示用户：

`git mergetool --no-prompt`

- 明确使用图形界面的合并工具（参见 `merge.guitool` 配置变量）：

`git mergetool --gui`

- 明确使用常规的合并工具（参见 `merge.tool` 配置变量）：

`git mergetool --no-gui`
