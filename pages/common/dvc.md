# dvc

> Data Version Control system for machine learning projects.
> Some subcommands such as `commit` have their own usage documentation.
> More information: <https://dvc.org/doc/command-reference>.

- Initialize a new DVC project:

`dvc init`

- Configure a remote storage location:

`dvc remote add {{storage_name}} {{url}}`

- Add one or more data files or directories to tracking:

`dvc add {{path/to/file_or_directory}}`

- Show project status:

`dvc status`

- Upload tracked files to remote storage:

`dvc push`

- Download tracked files from remote storage:

`dvc pull`

- Display help:

`dvc {{[-h|--help]}}`

- Display version:

`dvc --version`
