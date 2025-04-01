# pio test

> 在 PlatformIO 项目中运行本地测试。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>.

- 在当前 PlatformIO 项目的全部环境中运行所有测试：

`pio test`

- 仅在指定的环境中运行测试：

`pio test --environment {{environment1}} --environment {{environment2}}`

- 仅运行名称与特定通配符模式匹配的测试：

`pio test --filter "{{pattern}}"`

- 忽略名称与特定通配符模式匹配的测试：

`pio test --ignore "{{pattern}}"`

- 指定用于固件上传的端口：

`pio test --upload-port {{upload_port}}`

- 指定用于运行测试的自定义配置文件：

`pio test --project-conf {{path/to/platformio.ini}}`