# pio 测试

> 在 PlatformIO 项目上运行本地测试。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>。

- 在当前 PlatformIO 项目的所有环境中运行所有测试：

`pio test`

- 仅测试特定环境：

`pio test --environment {{environment1}} --environment {{environment2}}`

- 仅运行名称匹配特定 glob 模式的测试：

`pio test --filter "{{pattern}}"`

- 忽略名称匹配特定 glob 模式的测试：

`pio test --ignore "{{pattern}}"`

- 指定固件上传的端口：

`pio test --upload-port {{upload_port}}`

- 指定自定义配置文件以运行测试：

`pio test --project-conf {{path/to/platformio.ini}}`