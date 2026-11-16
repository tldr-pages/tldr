# gitman

> Language-agnostic dependency manager using Git.
> Clones repositories listed in `gitman.yml` and pins each one to a branch, tag, or commit.
> More information: <https://gitman.readthedocs.io>.

- Initialize a new `gitman.yml` configuration file in the current directory:

`gitman init`

- Install dependencies listed in `gitman.yml`:

`gitman install`

- Update all dependencies to their latest versions:

`gitman update`

- Update a specific dependency and all its nested dependencies:

`gitman update {{[-a|--all]}} {{dependency_name}}`

- Display the current version of each installed dependency:

`gitman list`

- Lock the current dependency versions into `gitman.yml`:

`gitman lock`

- Display the path to a specific installed dependency:

`gitman show {{dependency_name}}`

- Uninstall all installed dependencies:

`gitman uninstall`
