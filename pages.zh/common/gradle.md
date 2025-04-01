# gradle

> 一个开源的构建自动化系统。
> 更多信息：<https://gradle.org>.

- 编译一个包：

`gradle build`

- 排除测试任务：

`gradle build -x {{test}}`

- 以离线模式运行，防止 Gradle 在构建过程中访问网络：

`gradle build --offline`

- 清除构建目录：

`gradle clean`

- 以发布模式构建 Android 包 (APK)：

`gradle assembleRelease`

- 列出主要任务：

`gradle tasks`

- 列出所有任务：

`gradle tasks --all`