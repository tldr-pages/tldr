# flatpak ps

> List running applications and instances.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-ps>.

- List all running flatpak instances:

`flatpak ps`

- List only running instances for user-only installations:

`flatpak ps --user`

- Show the process ID of running instances (PID column):

`flatpak ps --columns={{application,pid}}`
