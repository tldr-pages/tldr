# dolt commit

> Commit staged changes to tables.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-commit>.

- Commit all staged changes, opening the editor specified by `$EDITOR` to enter the commit message:

`dolt commit`

- Commit all staged changes with the specified message:

`dolt commit --message "{{commit_message}}"`

- Stage all unstaged changes to tables before committing:

`dolt commit --all`

- Use the specified ISO 8601 commit date (defaults to current date and time):

`dolt commit --date "{{2021-12-31T00:00:00}}"`

- Use the specified author for the commit:

`dolt commit --author "{{author_name}} <{{author_email}}>"`

- Allow creating an empty commit, with no changes:

`dolt commit --allow-empty`

- Ignore foreign key warnings:

`dolt commit --force`
