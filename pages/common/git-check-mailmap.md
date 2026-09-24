# git check-mailmap

> Show canonical names and email addresses of contacts.
> More information: <https://git-scm.com/docs/git-check-mailmap>.

- Look up the canonical name associated with an email address:

`git check-mailmap {{email@example.com}}`

- Use the specified mailmap file in addition to the defaults:

`git check-mailmap --mailmap-file {{path/to/file}} {{email@example.com}}`
