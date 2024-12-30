# react-native start

> 命令行工具用于启动 React Native 服务器。
> 更多信息：<https://github.com/react-native-community/cli/blob/master/docs/commands.md#start>。

- 启动与连接设备通信的服务器：

`react-native start`

- 启动 metro 打包器并清除缓存：

`react-native start --reset-cache`

- 在自定义端口启动服务器（默认端口为 8081）：

`react-native start --port {{3000}}`

- 以详细模式启动服务器：

`react-native start --verbose`

- 指定用于转换文件的最大工作线程数（默认值为 CPU 核心数）：

`react-native start --max-workers {{count}}`

- 禁用交互模式：

`react-native start --no-interactive`