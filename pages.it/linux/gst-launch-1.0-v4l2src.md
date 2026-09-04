# gst-launch-1.0 v4l2src

> Legge fotogrammi da un dispositivo Video4Linux2.
> Maggiori informazioni: <https://gstreamer.freedesktop.org/documentation/video4linux2/v4l2src.html>.

- Visualizza video in una finestra:

`gst-launch-1.0 v4l2src device={{/dev/video0}} ! autovideosink`

- Crea un nodo PipeWire da un dispositivo v4l2:

`gst-launch-1.0 v4l2src device={{/dev/video0}} ! videoconvert ! pipewiresink mode=provide stream-properties="properties,media.class=Video/Source" client-name="{{Virtual Camera}}"`
