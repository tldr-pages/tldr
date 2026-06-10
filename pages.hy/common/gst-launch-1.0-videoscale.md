# gst-launch-1.0 տեսասանդղակ

> Չափափոխել վիդեո շրջանակները:.
> Լրացուցիչ տեղեկություններ. <https://gstreamer.freedesktop.org/documentation/videoconvertscale/videoscale.html>:.

- Տեսանյութի մասշտաբը՝ ինչպես մուտքագրման, այնպես էլ ելքի հնարավորություններին համապատասխանելու համար.:

`gst-launch-1.0 {{input}} ! videoscale ! {{output}}`

- Տեսանյութը չափավորել կամայական լուծման.:

`gst-launch-1.0 {{input}} ! videoscale ! video/x-raw,width={{width}},height={{height}} ! {{output}}`
