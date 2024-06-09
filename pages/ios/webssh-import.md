# webssh import

> Import SSH configuration on the WebSSH app through the mashREPL command-line.
> You may import the `ssh_config` file from other SSH clients by copying its contents to a new file using `malte`, before importing with this utility.
> This command can be only run under mashREPL menu on the WebSSH app.
> More information: <https://webssh.net/documentation/mashREPL/>.

- Apply a new SSH configuration from a `ssh_config` text file in the current directory (remove `--apply` for dry-run):

`webssh import sshconfig --apply`

- Apply a new SSH configuration from a specified text file (remove `--apply` for dry-run):

`webssh import sshconfig --from-file {{path/to/file}} --apply`

- Allow overwriting of current SSH connections configuration:

`webssh import sshconfig --from-file {{path/to/file}} --apply --overwrite`
