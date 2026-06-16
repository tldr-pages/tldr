# gst-launch-1.0 videoscale

> Resize video frames.
> More information: <https://gstreamer.freedesktop.org/documentation/videoconvertscale/videoscale.html>.

- Scale video to fit the capabilities of both input and output:

`gst-launch-1.0 {{input}} ! videoscale ! {{output}}`

- Scale video to an arbitrary resolution:

`gst-launch-1.0 {{input}} ! videoscale ! video/x-raw,width={{width}},height={{height}} ! {{output}}`
