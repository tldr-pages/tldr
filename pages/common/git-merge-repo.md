# git merge-repo

> Merge two repository histories.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-merge-repo>.

- Merge repository's branch into current repository's directory:

`git merge-repo {{local-path-to-repo.git}} {{branch-name}} {{path/to/directory}}`

- Merge remote repository's branch into current repository's directory, not preserving history:

`git merge-repo {{remote-path-to-repo}} {{branch-name}} .`
