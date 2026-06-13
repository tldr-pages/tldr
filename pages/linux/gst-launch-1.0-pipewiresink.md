# gst-launch-1.0 pipewiresink

> Create a PipeWire node to output data from.
> More information: <https://github.com/PipeWire/pipewire/tree/master/src/gst>.

- Output test video:

`gst-launch-1.0 videotestsrc ! pipewiresink mode=provide`

- Give the PipeWire node a name:

`gst-launch-1.0 {{source}} ! pipewiresink client-name={{node_name}}`
