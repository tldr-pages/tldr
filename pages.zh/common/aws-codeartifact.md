# aws codeartifact

> 管理 CodeArtifact 存储库、域、软件包、软件包版本和资产。
> CodeArtifact 是一个与常见包管理器和构建工具兼容的制品存储库，例如 Maven、Gradle、npm、Yarn、Twine、pip、NuGet 和 SwiftPM。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/codeartifact/>.

- 列出你的 AWS 账户中可用的域：

`aws codeartifact list-domains`

- 为指定的包管理器生成凭证：

`aws codeartifact login --tool {{npm|pip|twine}} --domain {{你的域}} --repository {{存储库名称}}`

- 获取 CodeArtifact 存储库的端点 URL：

`aws codeartifact get-repository-endpoint --domain {{你的域}} --repository {{存储库名称}} --format {{npm|pypi|maven|nuget|generic}}`

- 显示帮助信息：

`aws codeartifact help`

- 显示指定子命令的帮助信息：

`aws codeartifact {{子命令}} help`
