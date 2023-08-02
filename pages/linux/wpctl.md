# wpctl

> Manage WirePlumber, a session and policy manager for PipeWire.
> Note: you can use the special name `@DEFAULT_SINK@` in place of `id` to operate on the default sink.
> More information: <https://pipewire.pages.freedesktop.org/wireplumber/>.

- List all objects managed by WirePlumber:

`wpctl status`

- Print all properties of an object:

`wpctl inspect {{id}}`

- Set an object to be the default in its group:

`wpctl set-default {{id}}`

- Get the volume of a sink:

`wpctl get-volume {{id}}`

- Set the volume of a sink to `n` percent:

`wpctl set-volume {{id}} {{n}}%`

- Increase/Decrease the volume of a sink by `n` percent:

`wpctl set-volume {{id}} {{n}}%{{+|-}}`

- Mute/Unmute a sink (1 is mute, 0 is unmute):

`wpctl set-mute {{id}} {{1|0|toggle}}`
