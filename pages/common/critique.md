# critique

> Review Git changes with syntax highlighting and word-level diffs.
> More information: <https://github.com/remorses/critique#usage>.

- Review unstaged changes in the working tree:

`critique`

- Review only staged changes:

`critique --staged`

- Review the changes introduced by a specific commit:

`critique {{commit}}`

- Compare two branches:

`critique {{branch_1}} {{branch_2}}`

- Review the local `HEAD` against its remote-tracking branch:

`critique origin/{{branch}} HEAD`

- Review changes, automatically refreshing when files change:

`critique --watch`

- Restrict the review to files matching a glob pattern:

`critique --filter "{{src/**/*.ts}}"`

- Generate an AI code review using a specific agent:

`critique review --agent {{claude}}`
