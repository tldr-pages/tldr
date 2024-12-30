# roave-向后兼容性检查

> 验证两个版本的 PHP 库之间的向后兼容性破坏。
> 更多信息：<https://github.com/Roave/BackwardCompatibilityCheck>。

- 检查自上一个标签以来的破坏性更改：

`roave-backward-compatibility-check`

- 检查自特定标签以来的破坏性更改：

`roave-backward-compatibility-check --from={{git_reference}}`

- 检查自上一个标签与特定引用之间的破坏性更改：

`roave-backward-compatibility-check --to={{git_reference}}`

- 检查破坏性更改并输出为 Markdown：

`roave-backward-compatibility-check --format=markdown > {{results.md}}`