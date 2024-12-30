# osascript

> 运行 AppleScript 或 JavaScript 自动化 (JXA)。
> 更多信息：<https://keith.github.io/xcode-man-pages/osascript.1.html>。

- 运行一个 AppleScript 命令：

`osascript -e "{{say 'Hello world'}}"`

- 运行多个 AppleScript 命令：

`osascript -e "{{say 'Hello'}}" -e "{{say 'world'}}"`

- 运行编译的 (`*.scpt`)、打包的 (`*.scptd`) 或纯文本 (`*.applescript`) AppleScript 文件：

`osascript {{path/to/apple.scpt}}`

- 获取应用程序的包标识符 (对 `open -b` 很有用)：

`osascript -e 'id of app "{{Application}}"'`

- 运行一个 JavaScript 命令：

`osascript -l JavaScript -e "{{console.log('Hello world');}}"`

- 运行一个 JavaScript 文件：

`osascript -l JavaScript {{path/to/script.js}}`