# pw-metadata

> 监控、设置和删除 PipeWire 对象的元数据。
> 参见：`pipewire`，`pw-mon`，`pw-cli`。
> 更多信息：<https://docs.pipewire.org/page_man_pw-metadata_1.html>。

- 显示 `default` 名称下的元数据：

`pw-metadata`

- 显示 `settings` 中 ID 为 0 的元数据：

`pw-metadata {{[-n|--name]}} {{settings}} {{0}}`

- 列出所有可用的元数据对象：

`pw-metadata {{[-l|--list]}}`

- 持续运行并记录元数据的更改：

`pw-metadata {{[-m|--monitor]}}`

- 删除所有元数据：

`pw-metadata {{[-d|--delete]}}`

- 在 `settings` 中将 `log.level` 设置为 1：

`pw-metadata {{[-n|--name]}} {{settings}} {{0}} {{log.level}} {{1}}`

- 显示帮助：

`pw-metadata {{[-h|--help]}}`