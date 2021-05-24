# gh issue

> Create GitHub issues on a repository from the command-line.
> More information: <https://cli.github.com/manual/gh_issue_create>.

- Create a new issue for the current repository interactively:

`gh issue create`

- Create a new issue with a bug label interactively:

`gh issue create --label "{{bug}}"`

- Create a new issue interactively and assign it to 2 users:

`gh issue create --assignee {{user1,user2}}`

- Create a new issue with a title, body and assigned to the current user:

`gh issue create --title "{{title}}" --body "{{body}}" --assignee "{{@me}}"`

- Create a new issue interactively reading the body text from a file:

`gh issue create --body-file {{path/to/file}}`

- Create a new issue in the web browser:

`gh issue create --web`

- Display help:

`gh issue create --help`
