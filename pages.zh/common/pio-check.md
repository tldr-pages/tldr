# pio check

> 对 PlatformIO 项目执行静态分析检查。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>。

- 对当前项目执行基本分析检查：

`pio check`

- 对特定项目执行基本分析检查：

`pio check --project-dir {{project_dir}}`

- 对特定环境执行分析检查：

`pio check --environment {{environment}}`

- 执行分析检查并仅报告指定的缺陷严重程度类型：

`pio check --severity {{low|medium|high}}`

- 执行分析检查并在处理环境时显示详细信息：

`pio check --verbose`
