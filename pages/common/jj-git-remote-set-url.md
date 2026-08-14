# jj git remote set-url

> Set the URL of a Git remote.
> See also: `jj git remote add`, `jj git remote list`, `jj git remote remove`, `jj git remote rename`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-git-remote-set-url>.

- Set the fetch URL for a Git remote:

`jj git remote set-url {{remote_name}} {{remote_url}}`

- Set the push URL for a Git remote:

`jj git remote set-url --push {{push_url}} {{remote_name}}`

- Set both fetch and push URLs for a Git remote:

`jj git remote set-url --fetch {{fetch_url}} --push {{push_url}} {{remote_name}}`
