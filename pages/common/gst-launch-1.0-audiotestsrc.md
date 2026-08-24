# gst-launch-1.0 audiotestsrc

> Generate basic audio signals.
> More information: <https://gstreamer.freedesktop.org/documentation/audiotestsrc/index.html>.

- Generate and play a sine wave:

`gst-launch-1.0 audiotestsrc ! {{autoaudiosink}}`

- Define what type of wave to generate:

`gst-launch-1.0 audiotestsrc wave={{sine|square|saw|white-noise|pink-noise|ticks|...}} ! {{autoaudiosink}}`
