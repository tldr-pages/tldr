# git ignore

> Show/update `.gitignore` files.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-ignore>.

- Show global and local `.gitignore` files' content:

`git ignore`

- Ignore file(s) privately, updating `.git/info/exclude` file:

`git ignore {{file_pattern}} --private`

- Ignore file(s) locally, updating local `.gitignore` file:

`git ignore {{file_pattern}}`

- Ignore file(s) globally, updating global `.gitignore` file:

`git ignore {{file_pattern}} --global`
