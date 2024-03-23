# mesg

> Check or set a terminal's ability to receive messages from other users, usually from the `write` command.
> See also `write`, `talk`.
> More information: <https://manned.org/mesg.1>.

- Check terminal's openness to write messages:

`mesg`

- Disallow receiving messages from other users:

`mesg n`

- Allow receiving messages from other users:

`mesg y`

- Enable [v]erbose mode, printing a warning if the command is not executed from a terminal:

`mesg --verbose`
