# gst-launch-1.0 playbin

> Standalone media player.
> More information: <https://gstreamer.freedesktop.org/documentation/playback/playbin.html>.

- Play a local file:

`gst-launch-1.0 playbin uri=file:///{{path/to/file}}`

- Play a file from the internet:

`gst-launch-1.0 playbin uri={{https://example.com/path/to/file}}`

- Play track 4 of a CD:

`gst-launch-1.0 playbin uri=cdda://4`

- Play a DVD in a disc drive:

`gst-launch-1.0 playbin uri=dvd://`
