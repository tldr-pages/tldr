# xcode-select

> 在不同版本的 Xcode 和包含的开发工具之间切换。
> 还用于在安装后移动 Xcode 时更新其路径。
> 更多信息：<https://developer.apple.com/library/archive/technotes/tn2339/_index.html>。

- 安装 Xcode 的命令行工具：

`xcode-select --install`

- 选择给定路径作为活动开发目录：

`xcode-select --switch {{path/to/Xcode.app/Contents/Developer}}`

- 选择给定的 Xcode 实例，并将其开发目录作为活动目录：

`xcode-select --switch {{path/to/Xcode_file.app}}`

- 打印当前选择的开发目录：

`xcode-select --print-path`

- 丢弃任何用户指定的开发目录，以便通过默认搜索机制找到：

`sudo xcode-select --reset`