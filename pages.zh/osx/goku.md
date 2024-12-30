# goku

> 管理 Karabiner 配置。
> 更多信息：<https://github.com/yqrashawn/GokuRakuJoudo>。

- 使用默认配置生成 `karabiner.json`：

`goku`

- 使用特定的 `config.edn` 文件生成 `karabiner.json`：

`goku --config {{path/to/config.edn}}`

- 将新配置以干运行方式输出到 `stdout`，而不是更新 `karabiner.json`：

`goku --dry-run`

- 将整个配置以干运行方式输出到 `stdout`，而不是更新 `karabiner.json`：

`goku --dry-run-all`

- 显示帮助信息：

`goku --help`

- 显示版本：

`goku --version`