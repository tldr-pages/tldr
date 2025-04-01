# xcodes runtimes

> 管理 Xcode 模拟器运行时。
> 更多信息：<https://github.com/xcodesorg/xcodes>。

- 显示所有可用的模拟器运行时：

`xcodes runtimes --include-betas`

- 下载模拟器运行时：

`xcodes runtimes download {{runtime_name}}`

- 下载并安装模拟器运行时：

`xcodes runtimes install {{runtime_name}}`

- 为特定的 iOS/watchOS/tvOS/visionOS 版本下载/安装模拟器运行时（必须区分大小写）：

`xcodes runtimes {{download|install}} "{{iOS|watchOS|tvOS|visionOS}} {{runtime_version}}"`

- 设置运行时存档文件首次下载的特定位置（默认为 `~/Downloads`）：

`xcodes runtimes {{download|install}} {{runtime_name}} --directory {{path/to/directory}}`

- 在模拟器成功安装后不删除下载的存档文件：

`xcodes runtimes install {{runtime_name}} --keep-archive`
