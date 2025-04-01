# xed

> 在 Cinnamon 桌面环境中编辑文件。
> 更多信息: <https://github.com/linuxmint/xed>。

- 启动编辑器:

`xed`

- 打开特定文件:

`xed {{path/to/file1 path/to/file2 ...}}`

- 使用特定编码打开文件:

`xed --encoding {{WINDOWS-1252}} {{path/to/file1 path/to/file2 ...}}`

- 打印所有支持的编码:

`xed --list-encodings`

- 打开文件并定位到特定行:

`xed +{{10}} {{path/to/file}}`