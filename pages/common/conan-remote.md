# conan remote

> Manage the list of remotes (package servers) and the users authenticated on them.
> More information: <https://docs.conan.io/2/reference/commands/remote.html>.

- List the configured remotes in priority order:

`conan remote list`

- Add a new remote by name and URL:

`conan remote add {{remote_name}} {{remote_url}}`

- Log in to a remote, storing the credentials for a user:

`conan remote login {{remote_name}} {{username}}`

- Log out of a remote, removing the stored credentials:

`conan remote logout {{remote_name}}`

- Disable a remote without removing it:

`conan remote disable {{remote_name}}`

- Remove a remote from the list:

`conan remote remove {{remote_name}}`
