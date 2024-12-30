# pio 更新

> 更新已安装的 PlatformIO 核心包、开发平台和全局库。
> 另请参见：`pio platform update`，`pio lib update`。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/cmd_update.html>。

- 执行所有包、开发平台和全局库的完整更新：

`pio update`

- 仅更新核心包（跳过平台和库）：

`pio update --core-packages`

- 检查包、平台和库的新版本，但实际上不进行更新：

`pio update --dry-run`