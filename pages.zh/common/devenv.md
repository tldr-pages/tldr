# devenv

> 使用 Nix 创建快速、声明式、可重复和可组合的开发环境。
> 更多信息：<https://devenv.sh>。

- 初始化环境：

`devenv init`

- 以放宽的密闭性（气密状态）进入开发环境：

`devenv shell --impure`

- 获取当前环境的详细信息：

`devenv info --verbose`

- 使用 `devenv` 启动进程：

`devenv up --config /{{file}}/{{path}}/`

- 清理环境变量并以离线模式重新进入 shell：

`devenv --clean --offline`

- 删除以前的 shell 代：

`devenv gc`