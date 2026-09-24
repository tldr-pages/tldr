# gst-launch-1.0 uridecodebin

> Load data from an URI and automatically decode it.
> More information: <https://gstreamer.freedesktop.org/documentation/playback/uridecodebin.html>.

- Load and decode data from the internet:

`gst-launch-1.0 uridecodebin uri={{https://example.com/path/to/file}} ! {{sink}}`
