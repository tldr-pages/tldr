# zapier validate

> 验证一个 Zapier 集成。
> 更多信息：<https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#validate>。

- 验证一个集成：

`zapier validate`

- 在不进行样式检查的情况下验证一个集成：

`zapier validate --without-style`

- 在不运行构建脚本的情况下验证一个集成：

`zapier validate --skip-build`

- 使用额外的调试输出验证一个集成：

`zapier validate {{[-d|--debug]}}`

- 使用不同的输出结构验证一个集成：

`zapier validate {{[-f|--format]}} {{plain|json|raw|row|table}}`
