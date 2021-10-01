# git reauthor

> Replace details about an author identity, since this command rewrites git's history --force will be needed when `git push` is used.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-reauthor>.

- Replace the personal email and name of Jack to his work ones:

`git reauthor --old-email jack@perso.me --correct-email jack@work.com --correct-name 'Jack Foobar'`

- Replace the email and name of Jack to the ones defined in the Git config:

`git reauthor --old-email jack@perso.me --use-config`

- Set Jack's identity as the only one of the whole repository:

`git reauthor --all --correct-email jack@perso.me --correct-name Jack`

- Set Jack as the only committer of the whole repository (keeps authors):

`git reauthor --all --correct-email jack@perso.me --correct-name Jack --type committer`
