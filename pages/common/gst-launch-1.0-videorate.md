# gst-launch-1.0 videorate

> Normalize input framerate.
> More information: <https://gstreamer.freedesktop.org/documentation/videorate/index.html>.

- Normalize framerate and apply new timestamps:

`gst-launch-1.0 {{videotestsrc}} ! videorate ! {{autovideosink}}`

- Normalize framerate to 60 frames per second:

`gst-launch-1.0 {{videotestsrc}} ! videorate ! video/x-raw,framerate=60/1 ! {{autovideosink}}`
