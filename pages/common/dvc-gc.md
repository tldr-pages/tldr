# dvc gc

> Remove unused files and directories from cache or remote storage.
> More information: <https://dvc.org/doc/command-reference/gc>.

- Garbage collect from cache, keeping only version referenced by current workspace:

`dvc gc --workspace`

- Garbage collect from cache, keeping only version referenced by branch/tags/all_commits:

`dvc gc --all-branches --all-tags --all-commits`

- Garbage collect from cache, including default cloud remote storage (if set):

`dvc gc --all-commits --cloud`

- Garbage collect from cache, including specific cloud remote storage:

`dvc gc --all-commits --cloud -r {{remote_name}}`
