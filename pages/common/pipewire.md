# pipewire

> A server and user space API to deal with multimedia pipelines.
> More information: <https://docs.pipewire.org/>.

- Start the PipeWire daemon:

`pipewire`

- Start the PipeWire daemon with a specific configuration file:

`pipewire --config-file {{path/to/config.conf}}`

- List all audio and video devices:

`pw-cli info Device`

- List all nodes (sinks and sources):

`pw-cli info Node`

- Monitor PipeWire events in real-time:

`pw-mon`

- Display the graph of connected nodes:

`pw-dot | dot -Tsvg > pipewire.svg`
