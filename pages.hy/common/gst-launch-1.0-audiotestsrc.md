# gst-launch-1.0 audiotestsrc

> Ստեղծեք հիմնական աուդիո ազդանշաններ:.
> Լրացուցիչ տեղեկություններ. <https://gstreamer.freedesktop.org/documentation/audiotestsrc/index.html>:.

- Ստեղծեք և նվագարկեք սինուսային ալիք.:

`gst-launch-1.0 audiotestsrc ! {{autoaudiosink}}`

- Սահմանեք, թե ինչ տեսակի ալիք է առաջանում.:

`gst-launch-1.0 audiotestsrc wave={{sine|square|saw|white-noise|pink-noise|ticks|...}} ! {{autoaudiosink}}`
