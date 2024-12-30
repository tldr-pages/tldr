# xcodes 运行时

> 管理 Xcode 模拟器运行时。
> 更多信息：<https://github.com/xcodesorg/xcodes>。

- 显示所有可用的模拟器运行时：

`xcodes runtimes --include-betas`

- 下载一个模拟器运行时：

`xcodes runtimes download {{runtime_name}}`

- 下载并安装一个模拟器运行时：

`xcodes runtimes install {{runtime_name}}`

- 下载/安装特定 iOS/watchOS/tvOS/visionOS 版本的模拟器运行时（必须区分大小写）：

`xcodes runtimes {{download|install}} "{{iOS|watchOS|tvOS|visionOS}} {{runtime_version}}"`

- 设置运行时档案首次下载的特定位置（默认为 `~/Downloads`）：

`xcodes runtimes {{download|install}} {{runtime_name}} --directory {{path/to/directory}}`

- 在模拟器成功安装后，不删除下载的档案：

`xcodes runtimes install {{runtime_name}} --keep-archive`