# qtile

> A full-featured, hackable tiling window manager written and configured in Python.
> More information: <https://docs.qtile.org/en/latest/manual/commands/shell/index.html>.

- Start the window manager, if it is not running already (should ideally be run from `.xsession` or similar):

`qtile start`

- Check the configuration file for any compilation errors (default location is  `~/.config/qtile/config.py`):

`qtile check`

- Show current resource usage information:

`qtile top --force`

- Open the program `xterm` as a floating window on the group named `test-group`:

`qtile run-cmd --group {{test-group}} --float {{xterm}}`

- Restart the window manager:

`qtile cmd-obj --object cmd --function restart`
