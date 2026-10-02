# gst-inspect-1.0

> Print informatie over GStreamer-plugins.
> Meer informatie: <https://gstreamer.freedesktop.org/documentation/tools/gst-inspect.html>.

- Print informatie over een plugin:

`gst-inspect-1.0 {{plugin}}`

- Toon de hardware-transcodeermogelijkheden van je apparaat:

`gst-inspect-1.0 {{va|vaapi|nvcodec|...}}`

- Toon beschikbare containerplugins:

`gst-inspect-1.0 {{matroska|avi|ogg|isomp4|...}}`

- Toon beschikbare audiocodecs:

`gst-inspect-1.0 {{opus|vorbis|flac|...}}`

- Toon GStreamer-kernelementen:

`gst-inspect-1.0 coreelements`

- Toon plugins die gebruikmaken van grafische API's:

`gst-inspect-1.0 {{vulkan|opengl|...}}`

- Toon beschikbare beeldcodecs:

`gst-inspect-1.0 {{png|jpeg|...}}`

- Toon alle beschikbare plugins:

`gst-inspect-1.0`
