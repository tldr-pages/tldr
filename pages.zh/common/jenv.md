# jenv

> 管理”JAVA_HOME“环境变量的命令行工具。
> 更多信息： <https://www.jenv.be/>.

- 向 jEnv 添加一个 Java 版本：

`jenv add {{path/to/jdk_home}}`

- 显示当前使用的 JDK 版本：

`jenv version`

- 显示所有托管的 JDK：

`jenv versions`

- 设置全局JDK版本：

`jenv global {{java_version}}`

- 设置当前 shell 会话的 JDK 版本：

`jenv shell {{java_version}}`

- 启用 jEnv 插件：

`jenv enable-plugin {{plugin_name}}`
