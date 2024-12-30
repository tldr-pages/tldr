# pio 远程

> PlatformIO 远程开发的辅助命令。
> `pio remote [command]` 的参数与其本地执行的对应命令 `pio [command]` 相同。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/remote/index.html>。

- 列出所有活动的远程代理：

`pio remote agent list`

- 启动一个具有特定名称的新远程代理，并与朋友分享：

`pio remote agent start --name {{agent_name}} --share {{example1@example.com}} --share {{example2@example.com}}`

- 列出指定代理中的设备（省略 `--agent` 将指定所有代理）：

`pio remote --agent {{agent_name1}} --agent {{agent_name2}} device list`

- 连接到远程设备的串口：

`pio remote --agent {{agent_name}} device monitor`

- 在指定代理上运行所有目标：

`pio remote --agent {{agent_name}} run`

- 更新特定代理上安装的核心包、开发平台和全局库：

`pio remote --agent {{agent_name}} update`

- 在特定代理上运行所有环境中的所有测试：

`pio remote --agent {{agent_name}} test`