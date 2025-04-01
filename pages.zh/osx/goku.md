# goku

> 管理 Karabiner 配置。
> 更多信息：<https://github.com/yqrashawn/GokuRakuJoudo>.

- 使用默认配置生成 `karabiner.json`：

`goku`

- 使用特定的 `config.edn` 文件生成 `karabiner.json`：

`goku --config {{path/to/config.edn}}`

- 不更新 `karabiner.json`，而是将新配置输出到 `stdout`：

`goku --dry-run`

- 不更新 `karabiner.json`，而是将整个配置输出到 `stdout`：

`goku --dry-run-all`

- 显示帮助信息：

`goku --help`

- 显示版本信息：

`goku --version`
