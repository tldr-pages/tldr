# conan remote

> Manage the list of Conan remotes and the users authenticated on them.
> More information: <https://docs.conan.io/2/reference/commands/remote.html>.

- List the configured remotes:

`conan remote list`

- Add a remote:

`conan remote add {{remote_name}} {{url}}`

- Disable a remote without removing it:

`conan remote disable {{remote_name}}`

- Log in to a remote:

`conan remote login {{remote_name}}`

- Remove a remote:

`conan remote remove {{remote_name}}`
