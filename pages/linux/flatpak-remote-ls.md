# flatpak remote-ls

> List the applications and runtimes available in a remote repository.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remote-ls>.

- List all applications and runtimes available in all remotes:

`flatpak remote-ls`

- List all applications and runtimes available in a specific remote:

`flatpak remote-ls {{remote_name}}`

- List only applications in a specific remote:

`flatpak remote-ls --app {{remote_name}}`

- List only runtimes in a specific remote:

`flatpak remote-ls --runtime {{remote_name}}`

- List only applications and runtimes that have updates available:

`flatpak remote-ls --updates`

- List everything, including locale and debug extensions:

`flatpak remote-ls {{[-a|--all]}} {{remote_name}}`

- Show details such as architectures, branches, and commit IDs:

`flatpak remote-ls {{[-d|--show-details]}} {{remote_name}}`
