# gst-launch-1.0 pipewiresrc

> Read data from a Pipewire node.
> More information: <https://github.com/PipeWire/pipewire/tree/master/src/gst>.

- View video in a window:

`gst-launch-1.0 pipewiresrc target-object={{object_name}} ! autovideosink`

- Listen to the default microphone:

`gst-launch-1.0 pipewiresrc ! autoaudiosink`

- Record audio and video into a file

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc do-timestamp=true ! videoconvert ! {{vah264enc}} ! {{h264parse}} ! {{mux}}. pipewiresrc do-timestamp=true ! {{opusenc}} ! {{mux}}. {{matroskamux}} name={{mux}} ! filesink location={{path/to/file.mkv}}`
