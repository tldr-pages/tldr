# hyprlock

> GPU-accelerated screen locker for the Hyprland Wayland compositor.
> Configured via `~/.config/hypr/hyprlock.conf`.
> More information: <https://wiki.hypr.land/Hypr-Ecosystem/hyprlock/>.

- Lock the screen using the default configuration:

`hyprlock`

- Lock the screen using a specific configuration file:

`hyprlock {{[-c|--config]}} {{path/to/hyprlock.conf}}`

- Lock the screen immediately, bypassing the grace period:

`hyprlock --grace 0`

- Disable the fade-in animation when locking:

`hyprlock --no-fade-in`

- Display help:

`hyprlock {{[-h|--help]}}`
