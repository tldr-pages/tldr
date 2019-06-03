# pamixer

> A simple command-line mixer for PulseAudio.
> More information: <https://github.com/cdemoulins/pamixer>.

- List all sinks and sources with their corresponding IDs:

`pamixer --list-sinks --list-sources`

- Set the volume to 75% on the default sink:

`pamixer --set-volume {{75}}`

- Toggle mute on a sink other than the default:

`pamixer --toggle-mute --sink {{ID}}`

- Increase the volume on default sink by 5%:

`pamixer --increase {{5}}`

- Decrease the volume on a source by 5%:

`pamixer --decrease {{5}} --source {{ID}}`

- Use the allow boost option to increase, decrease, or set the volume above 100%:

`pamixer --set-volume {{105}} --allow-boost`

- Mute the default sink (use `--unmute` instead to unmute):

`pamixer --mute`
