# deemix

> Deezloader Remix의 나머지를 바탕으로 구축된 베어본 deezer 다운로드 라이브러리.
> 독립형 CLI 앱 또는 API를 사용하여 UI에서 구현 가능.
> 더 많은 정보: <https://gitlab.com/RemixDev/deemix-py>.

- 트랙이나 재생목록 다운로드:

`deemix {{https://www.deezer.com/us/track/00000000}}`

- 특정 비트전송률로 트랙/재생 목록 다운로드:

`deemix --bitrate {{FLAC|MP3}} {{url}}`

- 특정 경로로 다운로드:

`deemix --bitrate {{비트전송률}} --path {{경로}} {{url}}`

- 현재 디렉터리에 휴대용 deemix 구성 파일을 생성:

`deemix --portable --bitrate {{비트전송률}} --path {{경로}} {{url}}`
