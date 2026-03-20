# repo

> Manage multiple Git repositories with a single workflow.
> More information: <https://source.android.com/docs/setup/reference/repo>.

- Initialize a client checkout from a manifest repository:

`repo init -u {{manifest_repository_url}}`

- Synchronize all projects in the current checkout:

`repo sync`

- Synchronize only a specific project path:

`repo sync {{path/to/project}}`

- Create and switch to a topic branch in all projects:

`repo start {{branch_name}} --all`

- Run a Git command in every project managed by `repo`:

`repo forall -c '{{git status --short}}'`
