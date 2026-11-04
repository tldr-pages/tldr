# gst-launch-1.0 v4l2src

> Video4Linux2 장치에서 비디오 프레임을 읽어옴.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/video4linux2/v4l2src.html>.

- 비디오를 창에 표시:

`gst-launch-1.0 v4l2src device={{/dev/video0}} ! autovideosink`

- v4l2 장치를 PipeWire 노드로 생성:

`gst-launch-1.0 v4l2src device={{/dev/video0}} ! videoconvert ! pipewiresink mode=provide stream-properties="properties,media.class=Video/Source" client-name="{{가상 카메라}}"`
