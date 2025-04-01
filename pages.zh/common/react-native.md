# react-native

> 一个使用 React 构建原生应用的框架。
> 更多信息：<https://reactnative.dev>。

- 在同名目录中初始化一个新 React Native 项目：

`react-native init {{project_name}}`

- 启动 Metro 打包器：

`react-native start`

- 使用干净的缓存启动 Metro 打包器：

`react-native start --reset-cache`

- 构建当前应用并启动到连接的 Android 设备或模拟器上：

`react-native run-android`

- 构建当前应用并启动到 iOS 模拟器上：

`react-native run-ios`

- 以 `release` 模式构建当前应用并启动到连接的 Android 设备或模拟器上：

`react-native run-android --variant={{release}}`

- 启动 `logkitty` 并将日志打印到 `stdout`：

`react-native log-android`

- 启动 iOS 模拟器的 `tail system.log` 并将日志打印到 `stdout`：

`react-native log-ios`