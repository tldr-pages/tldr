# gst-launch-1.0 v4l2src

> خواندن فریم‌ها از دستگاه Video4Linux2.
> اطلاعات بیشتر: <https://gstreamer.freedesktop.org/documentation/video4linux2/v4l2src.html>.

- مشاهدهٔ ویدئو در پنجره:

`gst-launch-1.0 v4l2src device={{/dev/video0}} ! autovideosink`

- ایجاد گره PipeWire از دستگاه v4l2:

`gst-launch-1.0 v4l2src device={{/dev/video0}} ! videoconvert ! pipewiresink mode=provide stream-properties="properties,media.class=Video/Source" client-name="{{Virtual Camera}}"`
