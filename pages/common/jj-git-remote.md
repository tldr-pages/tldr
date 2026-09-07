# jj git remote

> Manage Git remotes.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-git-remote>.

- List all Git remotes:

`jj git remote list`

- Add a Git remote:

`jj git remote add {{remote_name}} {{remote_url}}`

- Add a Git remote with a specific push URL:

`jj git remote add --push-url {{push_url}} {{remote_name}} {{remote_url}}`

- Change the URL of a Git remote:

`jj git remote set-url {{remote_name}} {{remote_url}}`

- Set the push URL for a Git remote:

`jj git remote set-url --push {{push_url}} {{remote_name}}`

- Set both fetch and push URLs for a Git remote:

`jj git remote set-url --fetch {{fetch_url}} --push {{push_url}} {{remote_name}}`

- Remove a Git remote:

`jj git remote remove {{remote_name}}`

- Rename a Git remote:

`jj git remote rename {{old_name}} {{new_name}}`
