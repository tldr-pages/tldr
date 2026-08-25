# gst-launch-1.0 pulsesrc

> Pulseaudio 소스로부터 오디오 데이터 읽기.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/pulseaudio/pulsesrc.html>.

- 기본 마이크 입력 듣기:

`gst-launch-1.0 pulsesrc ! autoaudiosink`

- 이름으로 오디오 소스 지정 (부분 문자열 매칭 가능):

`gst-launch-1.0 pulsesrc device="{{장치_이름}}" ! autoaudiosink`

- 기본 오디오 출력 장치의 모니터 출력 녹음:

`gst-launch-1.0 pulsesrc device=@DEFAULT_MONITOR@ ! {{opusenc}} ! {{oggmux}} ! filesink location={{경로/대상/파일.ogg}}`
