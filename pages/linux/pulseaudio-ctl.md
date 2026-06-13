# pulseaudio-ctl

> Control PulseAudio volume.
> More information: <https://github.com/graysky2/pulseaudio-ctl>.

- Increase volume by 5%:

`pulseaudio-ctl up`

- Increase volume by a specific amount:

`pulseaudio-ctl up {{amount}}`

- Decrease volume by 5%:

`pulseaudio-ctl down`

- Decrease volume by a specific amount:

`pulseaudio-ctl down {{amount}}`

- Set volume to a specific percentage:

`pulseaudio-ctl set {{percentage}}`

- Set volume to a specific percentage if the current volume is higher than the provided value:

`pulseaudio-ctl atmost {{percentage}}`

- Toggle mute:

`pulseaudio-ctl mute`

- Toggle microphone mute:

`pulseaudio-ctl mute-input`
