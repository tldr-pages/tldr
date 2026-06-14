# diffstitch

> Compare multiple git branches against a base in a side-by-side HTML diff view.
> More information: <https://github.com/sroomberg/diffstitch>.

- Compare one or more branches against a base branch:

`diffstitch {{base_branch}} {{branch1}} {{branch2}}`

- Open the generated report in the browser immediately:

`diffstitch {{base_branch}} {{branch1}} --open`

- Write output to a custom directory:

`diffstitch {{base_branch}} {{branch1}} --output {{path/to/output}}`

- Set a custom title for the report page:

`diffstitch {{base_branch}} {{branch1}} --title "{{Report Title}}"`

- Print the version:

`diffstitch --version`
