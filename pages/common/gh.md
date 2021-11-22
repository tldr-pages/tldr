# gh

> Work seamlessly with GitHub from the command-line.
> Some subcommands such as `gh config` have their own usage documentation.
> More information: <https://cli.github.com/>.

- Clone a GitHub repository locally:

`gh repo clone {{owner}}/{{repository}}`

- Create a new issue:

`gh issue create`

- View and filter the open issues of the current repository:

`gh issue list`

- View an issue in the browser:

`gh issue view --web {{issue_number}}`

- Create a pull request:

`gh pr create`

- Create a pull request to a specified branch instead of the default:

`gh pr create --base {{dev}}`

- Locally check out the branch of a pull request, given its number:

`gh pr checkout {{pr_number}}`

- Check the status of a repository's pull requests:

`gh pr status`
