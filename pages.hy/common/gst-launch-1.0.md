# gst-launch-1.0

> Կառուցեք և գործարկեք GStreamer խողովակաշար:.
> Տես նաև՝ `gst-inspect-1.0`, `ffmpeg`:.
> Լրացուցիչ տեղեկություններ. <https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html>:.

- Նվագարկեք թեստային տեսանյութը պատուհանում.:

`gst-launch-1.0 videotestsrc ! autovideosink`

- Նվագարկեք թեստային աուդիո և միացրեք մանրամասն ելքը.:

`gst-launch-1.0 audiotestsrc {{[-v|--verbose]}} ! autoaudiosink`

- Նվագարկել մեդիա ֆայլը պատուհանում.:

`gst-launch-1.0 playbin uri={{protocol}}://{{host}}/{{path/to/file}}`

- Վերակոդավորել մեդիա ֆայլը.:

`gst-launch-1.0 filesrc location={{path/to/file}} ! {{file_type}}demux ! {{codec_type}}dec ! {{codec_type}}enc ! {{file_type}}mux ! filesink location={{path/to/file}}`

- Ֆայլի հոսք դեպի RTSP սերվեր.:

`gst-launch-1.0 filesrc location={{path/to/file}} ! rtspclientsink location=rtsp://{{host_ip}}/{{path/to/file}}`

- Հոսքի ավարտի իրադարձություն հարկադրել, եթե խողովակաշարը փակվի `<Ctrl c>`-ով այն բեռնարկղերի համար, որոնք պահանջում են վերջնականացում, օրինակ՝ `mp4`:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} videotestsrc ! x264enc ! mp4mux ! filesink location={{path/to/file.mp4}}`

- Multiplex միասին թեստային վիդեո և փորձարկման աուդիո ֆայլի մեջ.:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} videotestsrc ! {{x264enc}} ! {{element_name}}. audiotestsrc ! {{opusenc}} ! {{element_name}}. {{matroskamux}} name={{element_name}} ! filesink location={{path/to/file.mkv}}`

- Միացնել վրիպազերծման ելքը և խողովակաշարը նետել `.dot` ֆայլի մեջ, որն այնուհետև կարող է ներկայացվել այնպիսի գործիքներով, ինչպիսիք են `dot`:

`GST_DEBUG={{1..5}} GST_DEBUG_DUMP_DOT_DIR={{path/to/directory}} gst-launch-1.0 {{pipeline}}`
