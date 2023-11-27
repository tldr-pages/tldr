# hut

> A CLI tool for sourcehut.
> More information: <https://manned.org/hut>.

- Initialize `hut`'s configuration file (this will prompt for an OAuth2 access token, which is required to use `hut`):

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
