# jenv

> 管理 "JAVA_HOME" 环境变量。
> 更多信息：<https://www.jenv.be/>.

- 将 Java 版本添加到 jEnv：

`jenv add {{path/to/jdk_home}}`

- 显示当前使用的 JDK 版本：

`jenv version`

- 显示所有管理的 JDK：

`jenv versions`

- 设置全局 JDK 版本：

`jenv global {{java_version}}`

- 为当前 shell 会话设置 JDK 版本：

`jenv shell {{java_version}}`

- 启用 jEnv 插件：

`jenv enable-plugin {{plugin_name}}`