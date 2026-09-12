# git cherry

> Find commits that have yet to be applied upstream.
> More information: <https://git-scm.com/docs/git-cherry>.

- Show commits (and their messages) with equivalent commits upstream:

`git cherry {{[-v|--verbose]}}`

- Specify a different upstream and branch:

`git cherry {{origin}} {{specified_branch}}`

- Limit commits to those after a given commit:

`git cherry {{origin}} {{specified_branch}} {{limit_commit}}`
