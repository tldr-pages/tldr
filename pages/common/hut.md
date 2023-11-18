# hut

> A CLI tool for sourcehut.
> Use `hg` in place of `git` below if using mercurial.
> See `man hut` for more details.

- Initialize hut's configuration file:

`hut init`

- List git repositories:

`hut git list`

- Create a git repository:

`hut git create`

- List jobs on builds.sr.ht:

`hut builds list`

- Show a job's status:

`hut builds show {{job_id}}`

- SSH into a job container:

`hut ssh {{job_id}}`
