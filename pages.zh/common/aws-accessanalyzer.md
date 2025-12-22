# aws accessanalyzer

> 分析和审查资源策略，以识别潜在的安全风险。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/>.

- 创建一个新的 Access Analyzer：

`aws accessanalyzer create-analyzer --analyzer-name {{分析器名称}} --type {{类型}} --tags {{标签}}`

- 删除一个现有的 Access Analyzer：

`aws accessanalyzer delete-analyzer --analyzer-arn {{分析器_ARN}}`

- 获取指定 Access Analyzer 的详细信息：

`aws accessanalyzer get-analyzer --analyzer-arn {{分析器_ARN}}`

- 列出所有 Access Analyzer：

`aws accessanalyzer list-analyzers`

- 更新 Access Analyzer 的设置：

`aws accessanalyzer update-analyzer --analyzer-arn {{分析器_ARN}} --tags {{新标签}}`

- 创建一个新的 Access Analyzer 归档规则：

`aws accessanalyzer create-archive-rule --analyzer-arn {{分析器_ARN}} --rule-name {{规则名称}} --filter {{过滤器}}`

- 删除一个 Access Analyzer 归档规则：

`aws accessanalyzer delete-archive-rule --analyzer-arn {{分析器_ARN}} --rule-name {{规则名称}}`

- 列出所有 Access Analyzer 归档规则：

`aws accessanalyzer list-archive-rules --analyzer-arn {{分析器_ARN}}`
