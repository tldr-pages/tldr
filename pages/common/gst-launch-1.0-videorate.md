# gst-launch-1.0 videorate

> Normalize input framerate.
> More information: <https://gstreamer.freedesktop.org/documentation/videorate/index.html>.

- Normalize framerate and apply new timestamps:

`gst-launch-1.0 {{source}} ! videorate ! {{sink}}`

- Normalize framerate to 60 frames per second:

`gst-launch-1.0 {{source}} ! videorate ! video/x-raw,framerate=60/1 ! {{sink}}`
