# rtmpdump

> RTMP 프로토콜을 통해 스트리밍되는 미디어 콘텐츠 덤프.
> 더 많은 정보: <https://rtmpdump.mplayerhq.hu/rtmpdump.1.html>.

- 파일 다운로드:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-o|--flv]}} {{파일.ext}}`

- Flash 플레이어에서 파일 다운로드:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-W|--swfVfy]}} {{http://example.com/player}} {{[-f|--flashVer]}} "{{LNX 10,0,32,18}}" {{[-o|--flv]}} {{파일.ext}}`

- 연결 매개변수가 올바르게 감지되지 않는 경우 지정:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-a|--app]}} {{앱_이름}} {{[-y|--playpath]}} {{경로/대상/비디오}} {{[-o|--flv]}} {{파일.ext}}`

- 참조자를 요구하는 서버에서 파일 다운로드:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-p|--pageUrl]}} {{http://example.com/webpage}} {{[-o|--flv]}} {{파일.ext}}`
