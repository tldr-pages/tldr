# xcode-select

> 在不同版本的 Xcode 和包含的开发者工具之间进行切换。
> 也可以在 Xcode 安装后如果移动了位置时更新其路径。
> 更多信息：<https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- 安装 Xcode 的命令行工具：

`xcode-select --install`

- 选择一个指定的路径作为活动的开发者目录：

`xcode-select --switch {{path/to/Xcode.app/Contents/Developer}}`

- 选择一个指定的 Xcode 实例，并使用其开发者目录作为活动目录：

`xcode-select --switch {{path/to/Xcode_file.app}}`

- 打印当前选择的开发者目录：

`xcode-select --print-path`

- 丢弃任何用户指定的开发者目录，以便通过默认的搜索机制找到：

`sudo xcode-select --reset`
