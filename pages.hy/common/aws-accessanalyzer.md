# aws աքսեսուարային անալիզատոր

> Վերլուծել և վերանայել ռեսուրսների քաղաքականությունը՝ բացահայտելու անվտանգության հնարավոր ռիսկերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/>:.

- Ստեղծեք նոր Access Analyzer.:

`aws accessanalyzer create-analyzer --analyzer-name {{analyzer_name}} --type {{type}} --tags {{tags}}`

- Ջնջել առկա Access Analyzer:

`aws accessanalyzer delete-analyzer --analyzer-arn {{analyzer_arn}}`

- Ստացեք մանրամասներ հատուկ մուտքի անալիզատորի մասին.:

`aws accessanalyzer get-analyzer --analyzer-arn {{analyzer_arn}}`

- Թվարկեք բոլոր մուտքի անալիզատորները.:

`aws accessanalyzer list-analyzers`

- Թարմացրեք Access Analyzer-ի կարգավորումները.:

`aws accessanalyzer update-analyzer --analyzer-arn {{analyzer_arn}} --tags {{new_tags}}`

- Ստեղծեք նոր Access Analyzer արխիվի կանոն.:

`aws accessanalyzer create-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}} --filter {{filter}}`

- Ջնջել Access Analyzer արխիվի կանոնը.:

`aws accessanalyzer delete-archive-rule --analyzer-arn {{analyzer_arn}} --rule-name {{rule_name}}`

- Նշեք Access Analyzer-ի արխիվի բոլոր կանոնները.:

`aws accessanalyzer list-archive-rules --analyzer-arn {{analyzer_arn}}`
