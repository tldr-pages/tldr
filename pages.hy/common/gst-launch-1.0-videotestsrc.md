# gst-launch-1.0 videotestsrc

> Ստեղծեք թեստային վիդեո տվյալներ:.
> Լրացուցիչ տեղեկություններ. <https://gstreamer.freedesktop.org/documentation/videotestsrc/index.html>:.

- Ստեղծեք տեսանյութ SMPTE գունավոր գծերով.:

`gst-launch-1.0 videotestsrc ! {{autovideosink}}`

- Սահմանեք, թե ինչ տեսակի թեստային տեսանյութ պետք է արտադրվի.:

`gst-launch-1.0 videotestsrc pattern={{smpte|snow|green|ball|circular|...}} ! {{autovideosink}}`
