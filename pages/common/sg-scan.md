# sg scan

> Scan and rewrite code using ast-grep rule configurations.
> More information: <https://ast-grep.github.io/reference/cli/scan.html>.

- Scan the codebase with all configured rules:

`sg scan`

- Scan the codebase with a single rule file:

`sg scan --rule {{path/to/rule.yml}}`

- Scan with an inline rule definition:

`sg scan --inline-rules '{{id: no-console, language: javascript, rule: {pattern: "console.log($ARG)"}}}'`

- Interactively review and apply fixes:

`sg scan --interactive`

- Apply all fixes without confirmation:

`sg scan --update-all`

- Output results in SARIF format:

`sg scan --format {{sarif}}`

- Scan only rules matching a filter regex:

`sg scan --filter '{{rule_id_regex}}'`

- Output results as JSON with rule metadata:

`sg scan --json --include-metadata`
