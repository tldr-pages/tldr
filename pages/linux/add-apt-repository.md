# add-apt-repository

> Manages apt repository definitions.

- Add a new apt repository:

`add-apt-repository {{repository_spec}}`

- Remove an apt repository:

`add-apt-repository --remove {{repository_spec}}`

- Update the package cache after adding a repository:

`add-apt-repository --update {{repository_spec}}`

- Enable source packages:

`add-apt-repository --enable-source {{repository_spec}}`
