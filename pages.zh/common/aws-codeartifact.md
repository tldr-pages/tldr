# aws codeartifact

> 管理 CodeArtifact 仓库、域、软件包、软件包版本和资产。
> CodeArtifact 是一个与流行的包管理器和构建工具（如 Maven、Gradle、npm、Yarn、Twine、pip、NuGet 和 SwiftPM）兼容的工件存储库。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- 列出您的 AWS 账户中可用的域：

`aws codeartifact list-domains`

- 为特定的包管理器生成凭证：

`aws codeartifact login --tool {{npm|pip|twine}} --domain {{your_domain}} --repository {{repository_name}}`

- 获取 CodeArtifact 仓库的终结点 URL：

`aws codeartifact get-repository-endpoint --domain {{your_domain}} --repository {{repository_name}} --format {{npm|pypi|maven|nuget|generic}}`

- 显示帮助：

`aws codeartifact help`

- 显示特定子命令的帮助：

`aws codeartifact {{subcommand}} help`