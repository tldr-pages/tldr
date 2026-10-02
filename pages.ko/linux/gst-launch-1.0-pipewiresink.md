# gst-launch-1.0 pipewiresink

> 데이터를 출력하기 위한 PipeWire 노드를 생성.
> 더 많은 정보: <https://github.com/PipeWire/pipewire/tree/master/src/gst>.

- 테스트 비디오 출력:

`gst-launch-1.0 videotestsrc ! pipewiresink mode=provide`

- PipeWire 노드 이름 지정:

`gst-launch-1.0 {{소스파일}} ! pipewiresink client-name={{노드_이름}}`
