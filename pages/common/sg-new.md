# sg new

> Create new ast-grep projects, rules, tests, or utility rules.
> More information: <https://ast-grep.github.io/reference/cli/new.html>.

- Create a new ast-grep project interactively:

`sg new project`

- Create a new rule:

`sg new rule {{rule_id}}`

- Create a new rule for a specific language:

`sg new rule {{rule_id}} --lang {{javascript}}`

- Create a new test case:

`sg new test {{test_name}}`

- Create a new global utility rule:

`sg new util {{util_name}} --lang {{typescript}}`

- Accept all defaults without interactive input:

`sg new rule {{rule_id}} --lang {{python}} --yes`
