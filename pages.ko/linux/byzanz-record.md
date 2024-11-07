# byzanz-record

> 화면을 녹화합니다.
> 더 많은 정보: <https://manned.org/byzanz-record>.

- 화면을 녹화하고 파일에 기록 (기본적으로 `byzanz-record`는 10초만 녹화합니다):

`byzanz-record {{경로/대상/파일.[byzanz|flv|gif|ogg|ogv|webm]}}`

- 녹화 중 및 녹화 후 정보를 표시:

`byzanz-record --verbose {{경로/대상/파일.[byzanz|flv|gif|ogg|ogv|webm]}}`

- 화면을 1분 동안 녹화:

`byzanz-record --duration 60 {{경로/대상/파일.[byzanz|flv|gif|ogg|ogv|webm]}}`

- 녹화를 10초 지연 후 시작:

`byzanz-record --delay 10 {{경로/대상/파일.[byzanz|flv|gif|ogg|ogv|webm]}}`
