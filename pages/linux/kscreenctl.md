# kscreenctl

> Manage display outputs on KDE Plasma.
> See also: `kscreen-doctor`, `kscreen-console`.
> More information: <https://invent.kde.org/plasma/kscreen>.

- List all connected outputs:

`kscreenctl list-outputs`

- Show an on-screen label on each monitor to identify connector names:

`kscreenctl identify`

- Show information about a specific output (or use `active-output` / `primary-output`):

`kscreenctl {{DP-1}}`

- Set the resolution and refresh rate of an output:

`kscreenctl {{DP-1}} set-mode 1920x1080@60`

- Set the scale of an output to 200%:

`kscreenctl {{DP-1}} set-scale 200%`

- Place an output to the right of another:

`kscreenctl {{HDMI-A-1}} right-of {{DP-1}}`

- Disable a specific output:

`kscreenctl {{HDMI-A-1}} set-enabled false`

- Turn all outputs off through Display Power Management Signaling:

`kscreenctl off`
