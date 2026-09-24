# gst-launch-1.0

> GStreamer 파이프라인 생성 및 실행.
> 관련 항목: `gst-inspect-1.0`, `ffmpeg`.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html>.

- 테스트 비디오를 창에서 재생:

`gst-launch-1.0 videotestsrc ! autovideosink`

- 테스트 오디오 재생 및 자세한 출력 활성화:

`gst-launch-1.0 audiotestsrc {{[-v|--verbose]}} ! autoaudiosink`

- 미디어 파일을 창에서 재생:

`gst-launch-1.0 playbin uri={{프로토콜}}://{{호스트}}/{{경로/대상/파일}}`

- 미디어 파일 재인코딩:

`gst-launch-1.0 filesrc location={{경로/대상/파일}} ! {{파일_타입}}demux ! {{코덱_파일}}dec ! {{코덱_파일}}enc ! {{파일_타입}}mux ! filesink location={{경로/대상/파일}}`

- 파일을 RTSP 서버로 스트리밍:

`gst-launch-1.0 filesrc location={{경로/대상/파일}} ! rtspclientsink location=rtsp://{{host_ip}}/{{경로/대상/파일}}`

- `<Ctrl c>`로 종료 시 MP4 같은 컨테이너의 마무리를 위해 EOS(End Of Stream) 이벤트 강제 전송:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} videotestsrc ! x264enc ! mp4mux ! filesink location={{경로/대상/파일.mp4}}`

- 테스트 비디오와 테스트 오디오를 하나의 파일로 멀티플렉싱:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} videotestsrc ! {{x264enc}} ! {{요소_이름}}. audiotestsrc ! {{opusenc}} ! {{요소_이름}}. {{matroskamux}} name={{요소_이름}} ! filesink location={{경로/대상/파일.mkv}}`

- 디버그 출력 활성화 및 파이프라인을 `.dot` 파일로 덤프하여 `dot` 같은 도구로 렌더링 가능하게 저장:

`GST_DEBUG={{1..5}} GST_DEBUG_DUMP_DOT_DIR={{경로/대상/디렉터리}} gst-launch-1.0 {{파이프라인}}`
