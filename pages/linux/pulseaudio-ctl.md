# pulseaudio-ctl

> Control PulseAudio volume from the command line.
> More information: <https://github.com/graysky2/pulseaudio-ctl>.

- Increase volume by 5%:

`pulseaudio-ctl up`

- Increase volume by a specific amount:

`pulseaudio-ctl up {{10}}`

- Decrease volume by 5%:

`pulseaudio-ctl down`

- Decrease volume by a specific amount:

`pulseaudio-ctl down {{10}}`

- Set volume to a specific percentage:

`pulseaudio-ctl set {{50}}`

- Set volume to at most a specific percentage:

`pulseaudio-ctl atmost {{100}}`

- Toggle mute:

`pulseaudio-ctl mute`

- Toggle microphone mute:

`pulseaudio-ctl mute-input`
