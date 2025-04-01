# sonar-scanner

> 适用于不使用 Maven、Gradle 或 Ant 等构建工具的 SonarQube 项目的通用扫描工具。
> 更多信息：<https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/>.

- 使用项目根目录中的 `sonar-project.properties` 配置文件扫描项目：

`sonar-scanner`

- 使用非 `sonar-project.properties` 的配置文件扫描项目：

`sonar-scanner -D{{project.settings=myproject.properties}}`

- 打印调试信息：

`sonar-scanner -X`

- 显示帮助：

`sonar-scanner -h`
