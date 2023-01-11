# gh gist

> Work with GitHub Gists on the command-line.
> More information: <https://cli.github.com/manual/gh_gist>.

- Create a new Gist from specific files:

`gh gist create {{path/to/file1}} {{path/to/file2 path/to/file3 ...}}`

- Create a new Gist with a specific [desc]ription:

`gh gist create {{path/to/file1}} {{path/to/file2 path/to/file3 ...}} --desc "{{description}}"`

- Edit a specific Gist:

`gh gist edit {{id|url}}`

- List Gists owned by the currently logged in user:

`gh gist list --limit {{1..n}}`

- View a Gist in the default browser without rendering Markdown:

`gh gist view {{id|url}} --web --raw`
