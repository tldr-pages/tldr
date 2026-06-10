# gst-launch-1.0 աուդիոմիքսեր

> Խառնել աուդիո հոսքերը միասին:.
> Լրացուցիչ տեղեկություններ. <https://gstreamer.freedesktop.org/documentation/audiomixer/audiomixer.html>:.

- Խառնել երկու աուդիո հոսքեր միասին.:

`gst-launch-1.0 {{audiotestsrc}} ! {{element_name}}. {{audiotestsrc}} ! {{element_name}}. audiomixer name={{element_name}} ! {{fakesink}}`
