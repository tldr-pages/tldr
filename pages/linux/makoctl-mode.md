# makoctl mode

> Manage notification modes in mako.
> Modes can be used to change notification behavior (e.g., do-not-disturb).
> More information: <https://manned.org/makoctl>.

- List all currently active modes:

`makoctl mode`

- Add one or more modes:

`makoctl mode -a {{do-not-disturb}}`

- Remove a mode:

`makoctl mode -r {{do-not-disturb}}`

- Toggle a mode (add if absent, remove if present):

`makoctl mode -t {{do-not-disturb}}`

- Set specific modes, replacing all current modes:

`makoctl mode -s {{mode1 mode2 ...}}`
