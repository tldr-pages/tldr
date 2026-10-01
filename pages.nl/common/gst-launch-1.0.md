# gst-launch-1.0

> Bouw en voer een GStreamer-pipeline uit.
> Zie ook: `gst-inspect-1.0`, `ffmpeg`.
> Meer informatie: <https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html>.

- Speel een testvideo af in een venster:

`gst-launch-1.0 videotestsrc ! autovideosink`

- Speel testaudio af en schakel uitgebreide uitvoer in:

`gst-launch-1.0 audiotestsrc {{[-v|--verbose]}} ! autoaudiosink`

- Speel een mediabestand af in een venster:

`gst-launch-1.0 playbin uri={{protocol}}://{{host}}/{{pad/naar/bestand}}`

- Codeer een mediabestand opnieuw:

`gst-launch-1.0 filesrc location={{pad/naar/bestand}} ! {{bestand_type}}demux ! {{codec_type}}dec ! {{codec_type}}enc ! {{bestand_type}}mux ! filesink location={{pad/naar/bestand}}`

- Stream een bestand naar een RTSP-server:

`gst-launch-1.0 filesrc location={{pad/naar/bestand}} ! rtspclientsink location=rtsp://{{host_ip}}/{{pad/naar/bestand}}`

- Forceer een End Of Stream-gebeurtenis als de pipeline wordt afgesloten met `<Ctrl c>`, voor containers die finalisatie vereisen zoals `mp4`:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} videotestsrc ! x264enc ! mp4mux ! filesink location={{pad/naar/bestand.mp4}}`

- Multiplex testvideo en testaudio samen in één bestand:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} videotestsrc ! {{x264enc}} ! {{element_naam}}. audiotestsrc ! {{opusenc}} ! {{element_naam}}. {{matroskamux}} name={{element_naam}} ! filesink location={{pad/naar/bestand.mkv}}`

- Schakel debug-uitvoer in en dump een pipeline naar een `.dot`-bestand dat vervolgens gerenderd kan worden met tools zoals `dot`:

`GST_DEBUG={{1..5}} GST_DEBUG_DUMP_DOT_DIR={{pad/naar/map}} gst-launch-1.0 {{pipeline}}`
