# git-maintenance

> Run tasks to optimize Git repository data.
> More information: <https://git-scm.com/docs/git-maintenance>.

- Initialize Git config values so any scheduled maintenance will start running on this repository:

`git maintenance register`

- Start running maintenance on the current repository:

`git maintenance start`

- Halt the background maintenance schedule for the current repository:

`git maintenance stop`

- Remove the current repository from background maintenance:

`git maintenance unregister`

- Run a specific maintenance task on the current repository:

`git maintenance run --task={{commit-graph|gc|incremental-repack|loose-objects|pack-refs|prefetch}}`
