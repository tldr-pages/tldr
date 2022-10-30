# pw-loopback

> Tool for creating loopback devices in pipewire.
> More information: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Create a loopback device with the default loopback behavior:

`pw-loopback`

- Create a loopback device that automatically connects to the speakers:

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}'`

- Create a loopback device that automatically connects to the microphone:

`pw-loopback -m '{{[FL FR]}}' --playback-props='{{media.class=Audio/Source}}'`

- Create a dummy loopback device that doesn't automatically connect to anything:

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}' --playback-props='{{media.class=Audio/Source}}'`

- Create a loopback device that automatically connects to the speakers and swaps the left and right channels between the sink and source:

`pw-loopback --capture-props='{{media.class=Audio/Sink audio.position=[FL FR]}}' --playback-props='{{audio.position=[FR FL]}}'`

- Create a loopback device that automatically connects to the microphone and swaps the left and right channels between the sink and source:

`pw-loopback --capture-props='{{audio.position=[FR FL]}}' --playback-props='{{media.class=Audio/Source audio.position=[FL FR]}}'`
