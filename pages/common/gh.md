# gh

> Work seamlessly with GitHub.
> Some subcommands such as `config` have their own usage documentation.
> More information: <https://cli.github.com/manual/gh>.

- Clone a GitHub repository locally:

`gh repo clone {{owner}}/{{repository}}`

- Create a new issue:

`gh issue {{[new|create]}}`

- View and filter the open issues of the current repository:

`gh issue {{[ls|list]}}`

- View an issue in the default web browser:

`gh issue view {{[-w|--web]}} {{issue_number|url}}`

- Create a pull request:

`gh pr {{[new|create]}}`

- View a pull request in the default web browser:

`gh pr view {{[-w|--web]}} {{pr_number|url|branch}}`

- Check out a specific pull request locally:

`gh {{[co|pr checkout]}} {{pr_number|url|branch}}`

- Check the status of a repository's pull requests:

`gh pr status`
