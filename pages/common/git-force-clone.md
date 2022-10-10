# git force-clone

> Provides the basic functionality of `git clone`, but if the destination git repository already exists it will force-reset it to resemble a clone of the remote.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-force-clone>.

- Clone a Git repository into a new folder:

`git force-clone -b {{main}} {{remote_repository_location}} {{path/to/directory}}`

- Clone a Git repository into an existing folder of a git repository, performing a force-reset to resemble it to the remote:

`git force-clone -b {{main}} {{https://github.com/tldr-pages/tldr}} {{./tldr}}`
