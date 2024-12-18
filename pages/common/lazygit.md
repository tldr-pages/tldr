# lazygit

> A simple terminal UI for Git commands, providing an intuitive interface for managing repositories.
> More information: <https://github.com/jesseduffield/lazygit>.

- Open lazygit in the current repository:

`lazygit`

- Open lazygit for a specific Git repository:

`lazygit --path {{path/to/repository}}`

- Start lazygit with focus on a specific panel (e.g., `status`, `branch`, `log`, `stash`):

`lazygit {{status|branch|log|stash}}`

- Print the default lazygit configuration:

`lazygit --config`

- Tail the lazygit logs (useful with debug mode in another terminal):

`lazygit --logs`

- Run lazygit in debug mode:

`lazygit --debug`

- Print the configuration directory:

`lazygit --print-config-dir`
