# gst-launch-1.0 pulsesrc

> Կարդացեք աուդիո տվյալները Pulseaudio աղբյուրից:.
> Լրացուցիչ տեղեկություններ. <https://gstreamer.freedesktop.org/documentation/pulseaudio/pulsesrc.html>:.

- Լսեք լռելյայն խոսափողին.:

`gst-launch-1.0 pulsesrc ! autoaudiosink`

- Նշեք աղբյուրը անունով (կարող է համապատասխանել ենթատողին).:

`gst-launch-1.0 pulsesrc device="{{device_name}}" ! autoaudiosink`

- Ձայնագրեք լռելյայն լվացարանի մոնիտորը.:

`gst-launch-1.0 pulsesrc device=@DEFAULT_MONITOR@ ! {{opusenc}} ! {{oggmux}} ! filesink location={{path/to/file.ogg}}`
