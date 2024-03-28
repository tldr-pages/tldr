# git force-clone

> Get the basic functionality of `git clone`, but if the destination Git repository already exists it will force-reset it to resemble a clone of the remote.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-force-clone>.

- Clone a Git repository into a new directory:

`git force-clone {{remote_repository_location}} {{path/to/directory}}`

- Clone a Git repository into a new directory, checking out an specific branch:

`git force-clone -b {{branch_name}} {{remote_repository_location}} {{path/to/directory}}`

- Clone a Git repository into an existing directory of a Git repository, performing a force-reset to resemble it to the remote and checking out an specific branch:

`git force-clone -b {{branch_name}} {{remote_repository_location}} {{path/to/directory}}`
