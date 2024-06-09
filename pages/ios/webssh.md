# webssh

> Manage, import, and export SSH configuration on the WebSSH app through the mashREPL command-line.
> This command can be only run under mashREPL menu on the WebSSH app.
> More information: <https://webssh.net/documentation/mashREPL/>.

- Print the current version of WebSSH:

`webssh version`

- Print the current version of WebSSH in full format (for diagnostics):

`webssh version full`

- Export the current SSH configuration into a text file (remove `--apply` for dry-run):

`webssh export sshconfig --apply`

- Apply a new SSH configuration from a `ssh_config` text file in the current directory (remove `--apply` for dry-run):

`webssh export sshconfig --apply`

- Apply a new SSH configuration from a specified text file (remove `--apply` for dry-run):

`webssh export sshconfig --from-file {{path/to/file}} --apply`

- Allow overwriting of current SSH connections configuration:

`webssh export sshconfig --from-file {{path/to/file}} --apply --overwrite`
