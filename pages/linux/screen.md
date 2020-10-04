# screen

> Multiplex terminals, run scripts in background in "detachable screens"
> More information: <https://linux.die.net/man/1/screen>.

- Start screen in detached (daemon) mode with logging enabled:

`screen -L -dmS <name>`

- Attach screen that might still be attached elsewhere (detach remote):

`screen -dr <name>`

- Attach screen that is attached elsewhere (don't detach remote, will use resolution of remote's window):

`screen -x <name>`

- Start screen in detached (daemon) mode and run a command:

`screen -dmS <name> [command]`
