# gst-launch-1.0 audiomixer

> Mix audio streams together.
> More information: <https://gstreamer.freedesktop.org/documentation/audiomixer/audiomixer.html>.

- Mix two audio streams together:

`gst-launch-1.0 {{audiotestsrc}} ! {{element_name}}. {{audiotestsrc}} ! {{element_name}}. audiomixer name={{element_name}} ! {{fakesink}}`
