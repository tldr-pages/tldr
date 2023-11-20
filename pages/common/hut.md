# hut

> A CLI tool for sourcehut.
> Note: Use `hg` in place of `git` below if using Mercurial. See `man hut` for additional details.
> More information: <https://manned.org/hut>.

- Initialize `hut`'s configuration file:

`hut init`

- List Git/Mercurial repositories:

`hut {{git|hg}} list`

- Create a public Git/Mercurial repository:

`hut {{git|hg}} create {{name}}`

- List jobs on <https://builds.sr.ht>:

`hut builds list`

- Show the status of a job:

`hut builds show {{job_id}}`

- SSH into a job container:

`hut ssh {{job_id}}`
