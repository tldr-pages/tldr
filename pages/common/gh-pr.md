# gh-pr

> Work seamlessly with GitHub from the command line.
> More information: <https://cli.github.com/>.

- Create a pull request:

`gh pr create`

- Check out pull requests locally:

`gh pr checkout {{pr_number}}`

- View the changes made in the PR:

`gh pr diff`

- Approve the pull request of the current branch:

`gh pr review --approve`

- Merge a PR if you're on the branch, removes the branch on local and remote:

`gh pr merge`
