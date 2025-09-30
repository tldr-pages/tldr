# pw-loopback

> Create loopback devices in PipeWire.
> More information: <https://docs.pipewire.org/page_man_pw-loopback_1.html>.

- Create a loopback device with the default loopback behavior:

`pw-loopback`

- Create a loopback device that automatically connects to the speakers:

`pw-loopback {{[-m|--channel-map]}} '{{[FL FR]}}' {{[-i|--capture-props]}} '{{media.class=Audio/Sink}}'`

- Create a loopback device that automatically connects to the microphone:

`pw-loopback {{[-m|--channel-map]}} '{{[FL FR]}}' {{[-o|--playback-props]}} '{{media.class=Audio/Source}}'`

- Create a dummy loopback device that doesn't automatically connect to anything:

`pw-loopback {{[-m|--channel-map]}} '{{[FL FR]}}' {{[-i|--capture-props]}} '{{media.class=Audio/Sink}}' {{[-o|--playback-props]}} '{{media.class=Audio/Source}}'`

- Create a loopback device that automatically connects to the speakers and swaps the left and right channels between the sink and source:

`pw-loopback {{[-i|--capture-props]}} '{{media.class=Audio/Sink audio.position=[FL FR]}}' {{[-o|--playback-props]}} '{{audio.position=[FR FL]}}'`

- Create a loopback device that automatically connects to the microphone and swaps the left and right channels between the sink and source:

`pw-loopback {{[-i|--capture-props]}} '{{audio.position=[FR FL]}}' {{[-o|--playback-props]}} '{{media.class=Audio/Source audio.position=[FL FR]}}'`
