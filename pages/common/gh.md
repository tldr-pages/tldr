# gh

> Work seamlessly with GitHub from the command line.
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

- View a pull request in the browser:

`gh pr view --web {{pr_number}}`

- Locally check out the branch of a pull request, given its number:

`gh pr checkout {{pr_number}}`

- Check the status of a repository's pull requests:

`gh pr status`
