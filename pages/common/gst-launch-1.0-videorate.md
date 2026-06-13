# gst-launch-1.0 videorate

> Normalize input framerate.
> More information: <https://gstreamer.freedesktop.org/documentation/videorate/index.html>.

- Normalize framerate and apply new timestamps:

`gst-launch-1.0 {{source}} ! videorate ! {{sink}}`
