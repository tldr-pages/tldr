# vainfo

> Display information from VA API driver .
> More information: <https://wiki.archlinux.org/title/Hardware_video_acceleration#Verifying_VA-API>.

- Show version and supported entrypoints:

`vainfo`

- Test a specific display protocol:

`vainfo --display {{wayland|x11|drm|...}}`

- Show available display protocols:

`vainfo --display help`

- Show all supported entrypoints:

`vainfo {{[-a|--all]}}`

- Display help:

`vainfo --help`
