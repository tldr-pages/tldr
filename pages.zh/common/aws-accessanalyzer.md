# aws accessanalyzer

> 分析和审查资源策略，以识别潜在的安全风险。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html>.

- 创建新的 Access Analyzer：

`aws accessanalyzer create-analyzer --analyzer-name {{analyzer_name}} --type {{type}} --tags {{tags}}`

- 删除现有的 Access Analyzer：

`aws accessanalyzer delete-analyzer --analyzer-arn {{analyzer_arn}}`

- 获取特定 Access Analyzer 的详细信息：

`aws accessanalyzer get-analyzer --analyzer-arn {{analyzer_arn}}`

- 列出所有 Access Analyzer：

`aws accessanalyzer list-analyzers`

- 更新 Access Analyzer 的设置：

`aws accessanalyzer update-analyzer --analyzer-arn {{analyzer_arn}} --tags {{new_tags}}`

- 创建新的 Access Analyzer 归档规则：

`aws accessanalyzer create-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}} --filter {{filter}}`

- 删除 Access Analyzer 归档规则：

`aws accessanalyzer delete-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}}`

- 列出所有 Access Analyzer 归档规则：

`aws accessanalyzer list-archive-rules --analyzer-arn {{analyzer_arn}}`