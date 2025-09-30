# gh issue create

> Create GitHub issues on a repository.
> More information: <https://cli.github.com/manual/gh_issue_create>.

- Create a new issue against the current repository interactively:

`gh issue {{[new|create]}}`

- Create a new issue with the `bug` label interactively:

`gh issue {{[new|create]}} {{[-l|--label]}} "bug"`

- Create a new issue interactively and assign it to the specified users:

`gh issue {{[new|create]}} {{[-a|--assignee]}} {{user1,user2,...}}`

- Create a new issue with a title, body and assign it to the current user:

`gh issue {{[new|create]}} {{[-t|--title]}} "{{title}}" {{[-b|--body]}} "{{body}}" {{[-a|--assignee]}} "@me"`

- Create a new issue interactively, reading the body text from a file:

`gh issue {{[new|create]}} {{[-F|--body-file]}} {{path/to/file}}`

- Create a new issue in the default web browser:

`gh issue {{[new|create]}} {{[-w|--web]}}`

- Display help:

`gh issue {{[new|create]}} {{[-h|--help]}}`
