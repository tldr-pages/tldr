# tpm2

> A single small executable that combines the various tpm2-tools.
> Some subcommands such as `pcrread`, `pcrreset`, etc. have their own usage documentation.
> More information: <https://manned.org/tpm2>.

- View documentation for :

`tldr tpm2 {{subcommand}}`

- Run a subcommand in verbose mode:

`tpm2 {{[-V|--verbose]}} {{subcommand}}`

- Run a subcommand without writing to `stdout`:

`tpm2 {{[-Q|--quiet]}} {{subcommand}}`

- Display help:

`tpm2 pcrreset {{[-h|--help]}}`

- Display version:

`tpm2 pcrreset {{[-v|--version]}}`
