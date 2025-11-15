# stty

> 设置终端设备接口的选项。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- 显示当前终端的所有设置：

`stty {{[-a|--all]}}`

- 设置行数或列数：

`stty {{rows|cols}} {{数量}}`

- 获取设备的实际传输速度：

`stty {{[-F|--file]}} {{路径/到/设备文件}} speed`

- 重置所有模式为当前终端的合理默认值：

`stty sane`

- 在原始模式和普通模式之间切换：

`stty {{raw|cooked}}`

- 关闭或开启字符回显：

`stty {{-echo|echo}}`

- 显示帮助信息：

`stty --help`
