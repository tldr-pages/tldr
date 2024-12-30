# sonar-scanner

> 一个通用的 SonarQube 项目扫描器，适用于不使用 Maven、Gradle 或 Ant 等构建工具的项目。
> 更多信息：<https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/>.

- 使用位于项目根目录中的配置文件 `sonar-project.properties` 扫描项目：

`sonar-scanner`

- 使用其他配置文件而非 `sonar-project.properties` 扫描项目：

`sonar-scanner -D{{project.settings=myproject.properties}}`

- 打印调试信息：

`sonar-scanner -X`

- 显示帮助信息：

`sonar-scanner -h`