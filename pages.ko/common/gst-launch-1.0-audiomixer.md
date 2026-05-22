# gst-launch-1.0 audiomixer

> 여러 오디오 스트림을 하나로 믹싱.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/audiomixer/audiomixer.html>.

- 두 개의 오디오 스트림을 함께 믹싱:

`gst-launch-1.0 {테스트용_오디오_소스}} ! {{요소_이름}}. {{테스트용_오디오_소스}} ! {{요소_이름}}. audiomixer name={{요소_이름}} ! {{데이터를 실제로 출력하지 않고 버리는(sink) 요소}}`
