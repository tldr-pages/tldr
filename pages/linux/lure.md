# lure

> A distro-agnostic build system and user repository for Linux.
> More information: <https://github.com/lure-sh/lure/blob/master/docs/usage.md>.

- Install a package:

`lure {{[in|install]}} {{package}}`

- Remove a package:

`lure {{[rm|remove]}} {{package}}`

- Update packages:

`lure {{[up|upgrade]}}`

- List all available packages:

`lure {{[ls|list]}}`

- Pull all repositories that have changed:

`lure {{[ref|refresh]}}`

- Add a new repository:

`lure {{[ar|addrepo]}} {{[-n|--name]}} {{repository_name}} --url {{repository_url}}`

- Remove an existing repository:

`lure {{[rr|removerepo]}} --name {{repository_name}}`

- Build a package:

`lure build -s {{path/to/script}}`
