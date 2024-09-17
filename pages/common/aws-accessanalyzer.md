# aws accessanalyzer

> Analyze and review resource policies to identify potential security risks.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html>.

- Create a new Access Analyzer:

`aws accessanalyzer create-analyzer --analyzer-name {{analyzer_name}} --type {{type}} --tags {{tags}}`

- Delete an existing Access Analyzer:

`aws accessanalyzer delete-analyzer --analyzer-arn {{analyzer_arn}}`

- Get details of a specific Access Analyzer:

`aws accessanalyzer get-analyzer --analyzer-arn {{analyzer_arn}}`

- List all Access Analyzers:

`aws accessanalyzer list-analyzers`

- Update settings of an Access Analyzer:

`aws accessanalyzer update-analyzer --analyzer-arn {{analyzer_arn}} --tags {{new_tags}}`

- Create a new Access Analyzer archive rule:

`aws accessanalyzer create-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}} --filter {{filter}}`

- Delete an Access Analyzer archive rule:

`aws accessanalyzer delete-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}}`

- List all Access Analyzer archive rules:

`aws accessanalyzer list-archive-rules --analyzer-arn {{analyzer_arn}}`
