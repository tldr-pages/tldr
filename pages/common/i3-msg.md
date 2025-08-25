# i3-msg

> Send messages to a running instance of i3 using IPC.
> See <https://i3wm.org/docs/userguide.html#list_of_commands> for available commands.
> More information: <https://manned.org/i3-msg>.

- Run an i3 command:

`i3-msg {{command}}`

- Print a list of workspaces in JSON:

`i3-msg -t get_workspaces`

- Print a layout tree of all open windows, containers, outputs, and workspaces in JSON:

`i3-msg -t get_tree`
