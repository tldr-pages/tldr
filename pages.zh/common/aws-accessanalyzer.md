# aws accessanalyzer

> 分析和审查资源策略，以识别潜在的安全风险。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html>。

- 创建一个新的访问分析器：

`aws accessanalyzer create-analyzer --analyzer-name {{analyzer_name}} --type {{type}} --tags {{tags}}`

- 删除一个现有的访问分析器：

`aws accessanalyzer delete-analyzer --analyzer-arn {{analyzer_arn}}`

- 获取特定访问分析器的详细信息：

`aws accessanalyzer get-analyzer --analyzer-arn {{analyzer_arn}}`

- 列出所有访问分析器：

`aws accessanalyzer list-analyzers`

- 更新访问分析器的设置：

`aws accessanalyzer update-analyzer --analyzer-arn {{analyzer_arn}} --tags {{new_tags}}`

- 创建一个新的访问分析器归档规则：

`aws accessanalyzer create-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}} --filter {{filter}}`

- 删除一个访问分析器归档规则：

`aws accessanalyzer delete-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}}`

- 列出所有访问分析器归档规则：

`aws accessanalyzer list-archive-rules --analyzer-arn {{analyzer_arn}}`