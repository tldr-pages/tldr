# git ls-remote

> Git command for listing references in a remote repository based on name or URL.
> If no name or URL are given, then the configured upstream branch will be used, or remote origin if the former is not configured.
> More information: <https://git-scm.com/docs/git-ls-remote.html>.

- Show all references in the default remote repository:

`git ls-remote`

- Show only heads references in the default remote repository:

`git ls-remote --heads`

- Show only tags references in the default remote repository:

`git ls-remote --tags`

- Show all references from a remote repository based on name or url:

`git ls-remote {{repository_url}}`

- Show references from a remote repository filtered by a pattern:

`git ls-remote {{repository_name}} "{{pattern}}"`
