# gradle

> 一个开源构建自动化系统。
> 更多信息：<https://gradle.org>。

- 编译一个包：

`gradle build`

- 排除测试任务：

`gradle build -x {{test}}`

- 以离线模式运行，以防止Gradle在构建期间访问网络：

`gradle build --offline`

- 清理构建目录：

`gradle clean`

- 在发布模式下构建Android包（APK）：

`gradle assembleRelease`

- 列出主要任务：

`gradle tasks`

- 列出所有任务：

`gradle tasks --all`