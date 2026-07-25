# kscreenctl

> Manage display outputs on KDE Plasma (intended replacement for `kscreen-doctor`).
> See also: `kscreen-doctor`, `kscreen-console`.
> More information: <https://invent.kde.org/plasma/kscreen/-/merge_requests/487>.

- Show an on-screen popup on each connected monitor to identify them:

`kscreenctl identify`

- Run a command against the currently active output:

`kscreenctl active-output calibrate-hdr`

- Run a command against a specific output:

`kscreenctl {{HDMI-A-1}} {{command}}`

- Display help:

`kscreenctl {{help|--help}}`
