# glab mr

> Manage GitLab merge requests from the command-line.
> Some subcommands such as `glab mr create` have their own usage documentation.
> More information: <https://glab.readthedocs.io/en/latest/mr>.

- Create a merge request:

`glab mr create`

- Check out a specific merge request locally:

`glab mr checkout {{mr_number}}`

- View the changes made in the merge request:

`glab mr diff`

- Approve the merge request for the current branch:

`glab mr approve`

- Merge the merge request associated with the current branch interactively:

`glab mr merge`

- Edit a merge request interactively:

`glab mr update`

- Edit the target branch of a merge request:

`glab mr update --target-branch {{branch_name}}`
