# roave-backward-compatibility-check

> 验证两个版本之间的 PHP 库的向后兼容性中断。
> 更多信息：<https://github.com/Roave/BackwardCompatibilityCheck>.

- 检查自上次标签以来的破坏性变更：

`roave-backward-compatibility-check`

- 检查自特定标签以来的破坏性变更：

`roave-backward-compatibility-check --from={{git_reference}}`

- 检查自上次标签到特定引用之间的破坏性变更：

`roave-backward-compatibility-check --to={{git_reference}}`

- 检查破坏性变更并以 Markdown 格式输出：

`roave-backward-compatibility-check --format=markdown > {{results.md}}`