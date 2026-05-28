# gst-launch-1.0 audiomixer

> 여러 오디오 스트림을 하나로 믹싱.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/audiomixer/audiomixer.html>.

- 두 개의 오디오 스트림을 함께 믹싱:

`gst-launch-1.0 {{audiotestsrc}} ! {{element_name}}. {{audiotestsrc}} ! {{element_name}}. audiomixer name={{element_name}} ! {{fakesink}}`
