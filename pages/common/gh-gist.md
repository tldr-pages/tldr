# gh gist

> Work with GitHub Gists on the command line.
> More information: <https://cli.github.com/manual/gh_gist>.

- Create new gist from file(s) - if multiple, separate by spaces:

`gh gist create {{filename}}`

- Create new gist with description:

`gh gist create {{filename}} -d "{{description}}"`

- Edit gist:

`gh gist edit {{ID or URL}}`

- List gists you own:

`gh gist list --limit {{int}}`

- View gist in browser without markdown:

`gh gist view {{ID or URL}} --web --raw`
