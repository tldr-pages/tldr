# hg

> Mercurial - a distributed source control management system.
> Some subcommands such as `commit` have their own usage documentation.
> More information: <https://www.mercurial-scm.org/help/commands>.

- Create an empty Mercurial repository:

`hg init`

- Clone a remote Mercurial repository from the internet:

`hg clone {{https://example.com/repo}}`

- View the status of a local repository:

`hg status`

- Add all new files to the next commit:

`hg add`

- Commit changes to version history:

`hg commit {{[-m|--message]}} {{message_text}}`

- Push local changes to a remote repository:

`hg push`

- Pull any changes made to a remote:

`hg pull`

- Reset everything the way it was in the latest commit:

`hg update {{[-C|--clean]}}; hg purge`
