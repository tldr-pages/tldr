# gst-inspect-1.0

> Print information on GStreamer plugins.
> More information: <https://gstreamer.freedesktop.org/documentation/tools/gst-inspect.html>.

- Print information on a plugin:

`gst-inspect-1.0 {{plugin}}`

- List hardware transcoding capabilities of your device:

`gst-inspect-1.0 {{vaapi|nvcodec}}`

- List available container plugins:

`gst-inspect-10 {{matroska|avi|ogg|isomp4}}`

- List available audio codecs:

`gst-inspect-1.0 {{opus|vorbis|flac}}`

- List GStreamer core elements:

`gst-inspect-1.0 coreelements`

- List plugins that utilize graphics APIs:

`gst-inspect-1.0 {{vulkan|opengl}}`

- List available image codecs:

`gst-inspect-1.0 {{png|jpeg}}`

- List all available plugins:

`gst-inspect-1.0`
