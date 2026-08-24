# gst-launch-1.0 fakesink

> 모든 데이터를 받아들이고 버리는 sink.
> 파이프라인의 어느 부분이 문제인지 테스트할 때 유용.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/coreelements/fakesink.html>.

- 출력 없이 파이프라인 데이터를 소비:

`gst-launch-1.0 {{파이프라인}} ! fakesink`

- 수신한 데이터 정보를 출력:

`gst-launch-1.0 {{[-v|--verbose]}} {{파이프라인}} ! fakesink silent=false`
