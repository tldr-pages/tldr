# gst-launch-1.0

> GStreamer 파이프라인 빌드 및 실행.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html>.

- 창에서 테스트 비디오 재생:

`gst-launch-1.0 videotestsrc ! xvimagesink`

- 창에서 미디어 파일 재생:

`gst-launch-1.0 playbin uri={{프로토콜}}://{{호스트}}/{{경로/대상/파일}}`

- 미디어 파일을 다시 인코딩:

`gst-launch-1.0 filesrc location={{경로/대상/파일}} ! {{파일_타입}}demux ! {{코덱_타입}}dec ! {{코덱_타입}}enc ! {{파일_타입}}mux ! filesink location={{경로/대상/파일}}`

- RTSP 서버로 파일 스트리밍:

`gst-launch-1.0 filesrc location={{경로/대상/파일}} ! rtspclientsink location=rtsp://{{호스트_아이피}}/{{경로/대상/파일}}`
