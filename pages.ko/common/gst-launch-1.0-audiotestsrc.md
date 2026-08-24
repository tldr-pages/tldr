# gst-launch-1.0 audiotestsrc

> 기본 오디오 신호 생성.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/audiotestsrc/index.html>.

- 사인파(sine wave) 생성 및 재생:

`gst-launch-1.0 audiotestsrc ! {{자동_오디오_출력요소}}`

- 생성할 파형 유형 지정:

`gst-launch-1.0 audiotestsrc wave={{sine|square|saw|white-noise|pink-noise|ticks|...}} ! {{자동_오디오_출력요소}}`
