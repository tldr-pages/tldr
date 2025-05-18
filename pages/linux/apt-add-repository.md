# apt-add-repository

> Manage `apt` repository definitions.
> More information: <https://manned.org/apt-add-repository.1>.

- Add a new `apt` repository:

`apt-add-repository {{repository_spec}}`

- Remove an `apt` repository:

`apt-add-repository {{[-r|--remove]}} {{repository_spec}}`

- Update the package cache after adding a repository:

`apt-add-repository --update {{repository_spec}}`

- Enable source packages:

`apt-add-repository {{[-s|--enable-source]}} {{repository_spec}}`
