# qrcp

> 파일 전송 도구.
> 더 많은 정보: <https://github.com/claudiodangelis/qrcp>.

- 파일 또는 폴더 전송:

`qrcp send {{경로/대상/파일_또는_폴더 경로/대상/파일_폴더 ...}}`

- 파일 수신:

`qrcp receive`

- 전송 전 콘텐츠 압축:

`qrcp send --zip {{경로/대상/파일_또는_폴더}}`

- 특정 [p]포트 사용:

`qrcp {{send|receive}} --port {{포트_번호}}`

- 특정 네트워크 [i]인터페이스 사용:

`qrcp {{send|receive}} --interface {{인터페이스}}`

- 서버를 계속 활성 상태로 유지:

`qrcp {{send|receive}} --keep-alive`
