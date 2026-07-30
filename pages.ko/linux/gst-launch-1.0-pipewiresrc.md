# gst-launch-1.0 pipewiresrc

> PipeWire 노드에서 데이터 읽어오기.
> 더 많은 정보: <https://github.com/PipeWire/pipewire/tree/master/src/gst>.

- 기본 마이크의 오디오 재생:

`gst-launch-1.0 pipewiresrc ! autoaudiosink`

- 지정한 노드의 비디오를 창에 표시:

`gst-launch-1.0 pipewiresrc target-object={{node_name}} ! autovideosink`

- 비디오를 파일로 녹화:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc ! videoconvert ! {{x264enc}} ! {{h264parse}} ! {{matroskamux}} ! filesink location={{경로/대상/파일.mkv}}`

- 비디오 노드에서 스크린샷 캡처:

`gst-launch-1.0 pipewiresrc num-buffers=1 ! videoconvert ! {{pngenc}} ! filesink location={{경로/대상/파일.png}}`

- 오디오를 파일로 녹음:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc ! {{opusenc}} ! {{oggmux}} ! filesink location={{경로/대상/파일.ogg}}`

- 장치의 모니터 출력을 녹음:

`gst-launch-1.0 pipewiresrc target-object={{node_name}} stream-properties=props,stream.capture.sink=true ! {{audioconvert ! fakesink}}`

- 오디오와 비디오를 하나의 파일로 멀티플렉싱(Multiplex)하여 저장:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc do-timestamp=true ! videoconvert ! {{x264enc}} ! {{h264parse}} ! {{mux}}. pipewiresrc do-timestamp=true ! {{opusenc}} ! {{mux}}. {{matroskamux}} name={{mux}} ! filesink location={{경로/대상/파일.mkv}}`
