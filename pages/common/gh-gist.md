# gh gist

> Work with GitHub Gists.
> More information: <https://cli.github.com/manual/gh_gist>.

- Create a new Gist from one or more files:

`gh gist create {{path/to/file1 path/to/file2 ...}}`

- Create a new Gist with a specific [desc]ription:

`gh gist create {{path/to/file1 path/to/file2 ...}} --desc "{{description}}"`

- Edit a Gist:

`gh gist edit {{id|url}}`

- List up to 42 Gists owned by the currently logged in user:

`gh gist list --limit {{42}}`

- View a Gist in the default browser without rendering Markdown:

`gh gist view {{id|url}} --web --raw`
