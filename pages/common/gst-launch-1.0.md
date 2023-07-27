# gst-launch-1.0

> Build and run a GStreamer pipeline.
> More information: <https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html?gi-language=c>.

- Play test video in a window:

`gst-launch-1.0 videotestsrc ! xvimagesink`

- Play a media file in a window:

`gst-launch-1.0 playbin uri={{protocol}}://{{host}}/{{path/to/file}}`

- Re-encode a media file:

`gst-launch-1.0 filesrc location={{path/to/file}} ! {{file_type}}demux ! {{codec_type}}dec ! {{codec_type}}enc ! {{file_type}}mux ! filesink location={{path/to/file}}`

- Stream a file to an RTSP server:

`gst-launch-1.0 filesrc location={{path/to/file}} ! rtspclientsink location=rtsp://{{host_IP}}/{{path/to/file}}`
