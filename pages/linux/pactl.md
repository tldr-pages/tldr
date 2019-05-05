# pactl

> Control a running PulseAudio sound server

- List all sinks (or other types - sinks are your outputs and sink-inputs are your current audio streams):

`pactl list sinks short`

- Change the default sink (output) to 1 (you can get the number from the list command)

`pactl set-default-sink 1`

- Move a sink-input 627 to sink 1

`pactl move-sink-input 627 1`

- Set the volume of sink 1 to 75%

`pactl set-sink-volume 1 0.75`

- Toggle mute on sink 1

`pactl set-sink-mute 1 toggle`
