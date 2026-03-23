# gst-launch-1.0 pulsesrc

> Read audio data from a Pulseaudio source.
> More information: <https://gstreamer.freedesktop.org/documentation/pulseaudio/pulsesrc.html>.

- Listen to the default microphone:

`gst-launch-1.0 pulsesrc ! autoaudiosink`

- Specify the source by name (can match a substring):

`gst-launch-1.0 pulsesrc device="{{device_name}}" ! autoaudiosink`

- Record the monitor of the default sink:

`gst-launch-1.0 pulsesrc device=@DEFAULT_MONITOR@ ! {{opusenc}} ! {{oggmux}} ! filesink location={{path/to/file.ogg}}`
