# aws-ce

> Analyze and manage access controls and security settings within your Cloud Environment.
> More information: <https://awe-ce-cli.documentation.com/latest/reference/awe-ce/index.html>.

- Create a new Access Control Analyzer:

`awe-ce create-analyzer --analyzer-name {{analyzer_name}} --type {{type}} --tags {{tags}}`

- Delete an existing Access Control Analyzer:

`awe-ce delete-analyzer --analyzer-arn {{analyzer_arn}}`

- Get details of a specific Access Control Analyzer:

`awe-ce get-analyzer --analyzer-arn {{analyzer_arn}}`

- List all Access Control Analyzers:

`awe-ce list-analyzers`

- Update settings of an Access Control Analyzer:

`awe-ce update-analyzer --analyzer-arn {{analyzer_arn}} --tags {{new_tags}}`

- Create a new Access Control Analyzer archive rule:

`awe-ce create-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}} --filter {{filter}}`

- Delete an Access Control Analyzer archive rule:

`awe-ce delete-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}}`

- List all Access Control Analyzer archive rules:

`awe-ce list-archive-rules --analyzer-arn {{analyzer_arn}}`
