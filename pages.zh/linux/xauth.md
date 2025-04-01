# xauth

> 编辑和显示用于连接到 X 服务器的授权信息。
> 更多信息：[manned.org/xauth](https://manned.org/xauth)。

- 使用特定的授权文件启动交互模式（默认为 `~/.Xauthority`）：

`xauth -f {{path/to/file}}`

- 显示授权文件的信息：

`xauth info`

- 显示所有显示的授权条目：

`xauth list`

- 为特定显示添加授权：

`xauth add {{display_name}} {{protocol_name}} {{key}}`

- 移除特定显示的授权：

`xauth remove {{display_name}}`

- 将当前显示的授权条目输出到 `stdout`：

`xauth extract - $DISPLAY`

- 将特定文件中的授权条目合并到授权数据库中：

`cat {{path/to/file}} | xauth merge -`

- 显示帮助：

`xauth --help`