# xcodes

> 下载、安装和管理多个 Xcode 版本。
> 参见：`xcodes runtimes`。
> 更多信息：<https://github.com/xcodesorg/xcodes>。

- 列出所有已安装的 Xcode 版本：

`xcodes installed`

- 列出所有可用的 Xcode 版本：

`xcodes list`

- 通过指定版本号或路径来选择一个 Xcode 版本：

`xcodes select {{xcode_version|path/to/Xcode.app}}`

- 下载并安装特定的 Xcode 版本：

`xcodes install {{xcode_version}}`

- 安装最新的 Xcode 版本并选择它：

`xcodes install --latest --select`

- 下载特定的 Xcode 版本存档到指定目录但不安装：

`xcodes download {{xcode_version}} --directory {{path/to/directory}}`
