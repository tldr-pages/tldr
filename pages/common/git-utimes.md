# git utimes

> Change files modification time to their last commit date. Does not touch files that are in the working tree or index.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-utimes>.

- Change all files modification time to their last commit date:

`git utimes`

- Change files modification time that are newer than their last commit date, preserving original modification time of files that were committed from the local repository:

`git utimes --newer`
