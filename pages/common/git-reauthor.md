# git reauthor

> Replace details about an author identity, since this command rewrites git's history --force will be needed when `git push` is used.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-reauthor>.

- Change the email and name:

`git reauthor --old-email {{old@example.com}} --correct-email {{new@example.com}} --correct-name "{{name}}"`

- Change the email and name to the ones defined in the Git config:

`git reauthor --old-email {{old@example.com}} --use-config`

- Change the email and name of all commits:

`git reauthor --all --correct-email {{name@example.com}} --correct-name {{name}}`
