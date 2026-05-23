# gst-launch-1.0 uridecodebin

> URI로부터 데이터를 로드하고 자동으로 디코딩.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/playback/uridecodebin.html>.

- 인터넷으로부터 데이터를 로드하고 디코딩 후 출력 장치(sink)로 전달:

`gst-launch-1.0 uridecodebin uri={{https://example.com/경로/대상/파일}} ! {{출력_장치}}`
