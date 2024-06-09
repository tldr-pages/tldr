# webssh

> Manage, import, and export SSH configuration on the WebSSH app through the mashREPL command-line.
> Some subcommands such as `webssh import` have their own usage documentation.
> This command can be only run under mashREPL menu on the WebSSH app.
> More information: <https://webssh.net/documentation/mashREPL/>.

- Print the current version of WebSSH:

`webssh version`

- Print the current version of WebSSH in full format (for diagnostics):

`webssh version full`

- Export the current SSH configuration into a text file (remove `--apply` for dry-run):

`webssh export sshconfig --apply`

- Restore WebSSH in-app purchases from the command-line:

`webssh store sync`

- Unregister WebSSH in-app purchases on the device (this does not constitute refunds):

`webssh store unregister all`
