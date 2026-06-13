# pw-config

> List configuration paths and sections that will be used by the PipeWire server and clients.
> More information: <https://docs.pipewire.org/page_man_pw-config_1.html>.

- List all configuration files that will be used:

`pw-config`

- List all configuration files that will be used by the PipeWire PulseAudio server:

`pw-config {{[-n|--name]}} pipewire-pulse.conf`

- List all configuration sections used by the PipeWire PulseAudio server:

`pw-config {{[-n|--name]}} pipewire-pulse.conf list`

- List the `context.properties` fragments used by the JACK clients:

`pw-config {{[-n|--name]}} jack.conf list context.properties`

- List the merged `context.properties` used by the JACK clients:

`pw-config {{[-n|--name]}} jack.conf merge context.properties`

- List the merged `context.modules` used by the PipeWire server and reformat:

`pw-config {{[-n|--name]}} pipewire.conf {{[-r|--recurse]}} merge context.modules`

- Display help:

`pw-config {{[-h|--help]}}`
