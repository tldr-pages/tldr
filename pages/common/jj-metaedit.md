# jj metaedit

> Modify the metadata of a revision without changing its content.
> See also: `jj describe`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-metaedit>.

- Update the author of the working-copy commit to the configured user:

`jj metaedit --update-author`

- Set a specific author on the working-copy commit:

`jj metaedit --author "{{name}} <{{email}}>"`

- Update the author date of a revision to the current time:

`jj metaedit --update-author-timestamp {{[-r|--revision]}} {{revset}}`

- Set the author date of a revision to a specific timestamp:

`jj metaedit --author-timestamp {{timestamp}} {{[-r|--revision]}} {{revset}}`

- Update the change description of a revision without opening an editor:

`jj metaedit {{[-m|--message]}} {{message}} {{[-r|--revision]}} {{revset}}`

- Generate a new change ID for a revision:

`jj metaedit --update-change-id {{[-r|--revision]}} {{revset}}`

- Force a commit to be rewritten, updating the committer details and timestamp:

`jj metaedit --force-rewrite {{[-r|--revision]}} {{revset}}`

- Update the author of multiple revisions to the configured user:

`jj metaedit --update-author {{revset1}} {{revset2}}`
