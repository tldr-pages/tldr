# react-native

> 一个用于使用 React 构建原生应用的框架。
> 更多信息：<https://reactnative.dev>。

- 在同名目录中初始化一个新的 React Native 项目：

`react-native init {{project_name}}`

- 启动 metro 打包工具：

`react-native start`

- 启动 metro 打包工具并清理缓存：

`react-native start --reset-cache`

- 在连接的 Android 设备或模拟器上构建当前应用并启动：

`react-native run-android`

- 在 iOS 模拟器上构建当前应用并启动：

`react-native run-ios`

- 以 `release` 模式构建当前应用并在连接的 Android 设备或模拟器上启动：

`react-native run-android --variant={{release}}`

- 启动 `logkitty` 并将日志打印到 `stdout`：

`react-native log-android`

- 启动 iOS 模拟器的 `tail system.log` 并将日志打印到 `stdout`：

`react-native log-ios`