# gh gist

> Work with GitHub Gists on the command line.
> More information: <https://cli.github.com/manual/gh_gist>.

- Create a new gist from a space-separated list of files:

`gh gist create {{path/to/files}}`

- Create a new gist with a description:

`gh gist create {{filename}} --desc "{{description}}"`

- Edit a gist:

`gh gist edit {{id_or_url}}`

- List gists you own:

`gh gist list --limit {{int}}`

- View a Gist in the default browser without rendering markdown:

`gh gist view {{id_or_url}} --web --raw`
