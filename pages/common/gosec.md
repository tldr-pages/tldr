# gosec

> Inspect Go source code for security problems.
> Note: `./...` is a Go package pattern understood by Go tooling. It matches the current package and all packages recursively under the current directory.
> More information: <https://github.com/securego/gosec>.

- Scan a Go package recursively in the current directory:

`gosec ./...`

- Scan a specific Go package:

`gosec {{path/to/package}}`

- Scan a Go package recursively and save results to a file:

`gosec -fmt {{json|yaml|csv|html|sonarqube|golint|sarif|junit-xml}} -out {{path/to/report}} {{./...}}`

- Only include a specific set of rules (by default, all rules will run):

`gosec -include {{G101,G203,G401,...}} {{./...}}`

- Exclude directories from scanning:

`gosec -exclude-dir {{path/to/excluded_directory}} {{./...}}`

- Scan with a specific severity or confidence level:

`gosec -severity {{low|medium|high}} -confidence {{low|medium|high}} {{./...}}`

- Exclude a specific set of rules from scanning:

`gosec -exclude {{G101,G304,G401,...}} {{./...}}`

- Scan test files as well:

`gosec -tests {{./...}}`
