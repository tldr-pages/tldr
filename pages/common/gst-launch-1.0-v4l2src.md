# gst-launch-1.0 v4l2src

> Read frames from a Video4Linux2 device.
> More information: <https://gstreamer.freedesktop.org/documentation/video4linux2/v4l2src.html>.

- View video in a window:

`gst-launch-1.0 v4l2src device={{/dev/video0}} ! autovideosink`

- Create a PipeWire node out of a v4l2 device:

`gst-launch-1.0 v4l2src device={{/dev/video0}} ! videoconvert ! pipewiresink mode=provide stream-properties="properties,media.class=Video/Source" client-name="{{Virtual Camera}}"`
