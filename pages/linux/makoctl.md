# makoctl

> Control the mako daemon.
> Sends IPC commands to the running mako daemon.
> Some subcommands such as `dismiss`, `invoke`, and `mode` have their own usage documentation.
> More information: <https://man.archlinux.org/man/makoctl.1.en>.

- List all current notifications:

`makoctl list`

- List notification history:

`makoctl history`

- Reload the mako configuration file:

`makoctl reload`

- Restore the most recently expired notification from history:

`makoctl restore`

- Display help and all available subcommands:

`makoctl help`

- View documentation for dismissing notifications:

`tldr makoctl-dismiss`

- View documentation for invoking notification actions:

`tldr makoctl-invoke`

- View documentation for managing modes:

`tldr makoctl-mode`
