# pw-loopback

> Tool for creating loopback devices in pipewire.
> More information: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Create a loopback device with the default loopback behavior:

`pw-loopback`

- Create a sink that can be selected in applications that forwards the data to another sink:

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink node.name=my-sink}}'`

- Create a sink that can be selected in applications that swaps the left and right channels to another sink:

`pw-loopback --capture-props='{{media.class=Audio/Sink node.name=my-sink audio.position=[FL FR]}}' --playback-props='{{audio.position=[FR FL]}}'`

- Create a source that can be selected in applications that swaps the left and right channels from another source:

`pw-loopback --capture-props='{{audio.position=[FR FL]}}' --playback-props='{{media.class=Audio/Source node.name=my-source audio.position=[FL FR]}}'`
