# git merge-repo

> Merge two repository histories.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-merge-repo>.

- Merge a repository's branch into the current repository's directory:

`git merge-repo {{path/to/repo}} {{branch_name}} {{path/to/directory}}`

- Merge a remote repository's branch into the current repository's directory, not preserving history:

`git merge-repo {{path/to/remote_repo}} {{branch_name}} .`
