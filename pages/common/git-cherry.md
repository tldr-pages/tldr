# git cherry

> Find commits that have yet to be applied upstream.
> More information: <https://git-scm.com/docs/git-cherry>.

- Show commits (and their messages) with equivalent commits upstream:

`git cherry -v`

- Specify a different upstream and topic branch:

`git cherry {{origin}} {{topic}}`

- Limit commits to those within a given limit:

`git cherry {{origin}} {{topic}} {{base}}`
