# spctl

> 管理安全评估策略子系统。
> 用于管理 macOS 中的 Gatekeeper。
> 更多信息：<https://keith.github.io/xcode-man-pages/spctl.8.html>.

- 关闭 Gatekeeper：

`spctl --master-disable`

- 添加规则以允许应用程序运行（规则标签是可选的）：

`spctl --add --label {{rule_name}} {{path/to/file}}`

- 打开 Gatekeeper：

`spctl --master-enable`

- 列出系统上的所有规则：

`spctl --list`