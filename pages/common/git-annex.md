# git annex

> Manage files with git, without checking their contents in.
> When a file is annexed, its content is moved into a key-value store, and a symlink is made that points to the content.
> More information: <https://git-annex.branchable.com/>.

- Help:

`git annex help`

- Initialize a repo with git annex:

`git annex init`

- Add file:

`git annex add {{path}}`

- Show status of files:

`git annex status {{path}}`

- Synchronize local repository with remote:

`git annex {{remote}}`

- Get file:

`git annex get {{path}}`
