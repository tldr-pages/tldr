# pamixer

> A simple command-line mixer for PulseAudio.

- List all sinks and sources with corresponding IDs:

`pamixer --list-sinks --list-sources`

- Set volume to 75% on the default sink:

`pamixer --set-volume {{75}}`

- Toggle mute on a sink other than the default:

`pamixer --toggle-mute --sink {{ID}}`

- Increase volume on default sink by 5%:

`pamixer --increase {{5}}`

- Decrease volume on a source by 5%:

`pamixer --decrease {{5}} --source {{ID}}`

- Use the allow boost option to increase/decrease/set volume above 100%:

`pamixer --set-volume {{105}} --allow-boost`

- Mute the default sink. If already muted it will stay muted.

`pamixer --mute`

- Unmute the default sink. If already unmuted it will stay unmuted.

`pamixer --unmute`
