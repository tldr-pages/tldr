# osascript

> 在命令行中运行指定的 AppleScript 或 JavaScript 脚本程序。
> 更多信息：<https://keith.github.io/xcode-man-pages/osascript.1.html>.

- 运行一个 AppleScript 命令：

`osascript -e "{{say '你好世界'}}"`

- 运行多条 AppleScript 命令：

`osascript -e "{{say '你好'}}" -e "{{say '世界'}}"`

- 运行一个已编译的脚本（`*.scpt`），包脚本（`*.scptd`），或明文的（`*.applescript`）AppleScript 文件：

`osascript {{目录 / 脚本文件.scpt}}`

- 获取应用程序的包名（这个包名，可以用在命令 `open -b` 中）：

`osascript -e 'id of app "{{应用程序名}}"'`

- 运行一个 JavaScript 命令：

`osascript -l JavaScript -e "{{console.log('你好世界！');}}"`

- 运行 JavaScript 文件：

`osascript -l JavaScript {{路径 / 文件名.js}}`
