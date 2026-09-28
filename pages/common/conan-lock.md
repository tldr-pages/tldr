# conan lock

> Create and manage lockfiles to pin dependencies for reproducible builds.
> More information: <https://docs.conan.io/2/reference/commands/lock.html>.

- Create a lockfile from the conanfile in a folder and write it to a file:

`conan lock create {{path/to/conanfile}} --lockfile-out={{conan.lock}}`

- Create a lockfile from a specific package reference:

`conan lock create --requires={{package_name}}/{{version}} --lockfile-out={{conan.lock}}`

- Add a requirement to an existing (or new) lockfile:

`conan lock add --requires={{package_name}}/{{version}} --lockfile={{conan.lock}} --lockfile-out={{conan.lock}}`

- Update the requirements of an existing lockfile to newer versions:

`conan lock update --lockfile={{conan.lock}} --lockfile-out={{conan.lock}}`

- Merge two or more lockfiles into a single one:

`conan lock merge --lockfile={{lock1.lock}} --lockfile={{lock2.lock}} --lockfile-out={{merged.lock}}`
