# git-maintenance

> Run tasks to optimize Git repository data.
> More information: <https://git-scm.com/docs/git-maintenance>.

- Register the current repository in the user's list of repositories to daily have maintenance run:

`git maintenance register`

- Schedule maintenance tasks on the current repository every hour:

`git maintenance start`

- Halt the background maintenance schedule for the current repository:

`git maintenance stop`

- Remove the current repository from the user's maintenance repository list:

`git maintenance unregister`

- Run a specific maintenance task on the current repository:

`git maintenance run --task={{commit-graph|gc|incremental-repack|loose-objects|pack-refs|prefetch}}`
