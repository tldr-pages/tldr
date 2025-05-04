# gh pr create

> Manage GitHub pull requests.
> More information: <https://cli.github.com/manual/gh_pr_create>.

- Interactively create a pull request:

`gh pr create`

- Create a pull request, determining the title and description from the commit messages of the current branch:

`gh pr create {{[-f|--fill]}}`

- Create a draft pull request:

`gh pr create {{[-d|--draft]}}`

- Create a pull request specifying the base branch, title, and description:

`gh pr create {{[-B|--base]}} {{base_branch}} {{[-t|--title]}} "{{title}}" {{[-b|--body]}} "{{body}}"`

- Start opening a pull request in the default web browser:

`gh pr create {{[-w|--web]}}`
