# git submodule

> Inspects, updates and manages submodules.
> More information: <https://git-scm.com/docs/git-submodule>.

- View existing submodules, and the checked-out commit for each one:

`git submodule status`

- Install a repository's submodules (listed in `.gitmodules`):

`git submodule update --init --recursive`

- Add a Git repository as a submodule of the current one:

`git submodule add {{repository_url}}`

- Add a Git repository as a submodule of the current one, at a specific directory:

`git submodule add {{repository_url}} {{path/to/directory}}`

- Update every submodule to its latest commit:

`git submodule update --init --recursive --remote`

- Change the URL of a submodule:

`git submodule set-url {{path/to/submodule}} {{new_url}}`

- Unregister a submodule (e.g. before removing it from the repository with `git rm`):

`git submodule deinit {{path/to/submodule}}`
