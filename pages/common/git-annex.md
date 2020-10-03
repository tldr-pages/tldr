# git annex

> Manage files with git, without checking their contents in.
> When a file is annexed, its content is moved into a key-value store, and a symlink is made that points to the content.
> More information: <https://git-annex.branchable.com>.

- Help:

`git annex help`

- Initialize a repo with git annex:

`git annex init`

- Add a file:

`git annex add {{path/to/file_or_directory}}`

- Show the current status of a file or directory:

`git annex status {{path/to/file_or_directory}}`

- Synchronize a local repository with a remote:

`git annex {{remote}}`

- Get a file or directory:

`git annex get {{path/to/file_or_directory}}`
