# gst-launch-1.0 pipewiresrc

> Read data from a PipeWire node.
> More information: <https://github.com/PipeWire/pipewire/tree/master/src/gst>.

- Listen to the default microphone:

`gst-launch-1.0 pipewiresrc ! autoaudiosink`

- Specify node to record and view video in a window:

`gst-launch-1.0 pipewiresrc target-object={{node_name}} ! autovideosink`

- Record video into a file:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc ! videoconvert ! {{x264enc}} ! {{h264parse}} ! {{matroskamux}} ! filesink location={{path/to/file.mkv}}`

- Capture a screenshot from a video node:

`gst-launch-1.0 pipewiresrc num-buffers=1 ! videoconvert ! {{pngenc}} ! filesink location={{path/to/file.png}}`

- Record audio into a file:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc ! {{opusenc}} ! {{oggmux}} ! filesink location={{path/to/file.ogg}}`

- Record the monitor of a device:

`gst-launch-1.0 pipewiresrc target-object={{node_name}} stream-properties=props,stream.capture.sink=true ! {{audioconvert ! fakesink}}`

- Multiplex audio and video into a file:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc do-timestamp=true ! videoconvert ! {{x264enc}} ! {{h264parse}} ! {{mux}}. pipewiresrc do-timestamp=true ! {{opusenc}} ! {{mux}}. {{matroskamux}} name={{mux}} ! filesink location={{path/to/file.mkv}}`
