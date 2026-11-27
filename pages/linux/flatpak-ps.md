# flatpak ps

> List running Flatpak instances.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-ps>.

- List running instances:

`flatpak ps`

- Show the application ID and the process ID of the sandbox for each instance:

`flatpak ps --columns application,child-pid`

- Show the runtime and its branch alongside each application ID:

`flatpak ps --columns application,runtime,runtime-branch`

- List the available columns:

`flatpak ps --columns help`
