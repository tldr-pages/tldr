# mitmdump

> HTTP 트래픽을 보기, 기록 및 프로그래밍적으로 변환.
> mitmproxy의 명령줄 대응 도구.
> 더 많은 정보: <https://docs.mitmproxy.org/stable/#mitmdump>.

- 프록시를 시작하고 모든 출력을 파일에 저장:

`mitmdump -w {{경로/대상/파일}}`

- 저장된 트래픽 파일에서 POST 요청만 필터링:

`mitmdump -nr {{입력_파일_이름}} -w {{출력_파일_이름}} "{{~m post}}"`

- 저장된 트래픽 파일 재생:

`mitmdump -nc {{경로/대상/파일}}`
