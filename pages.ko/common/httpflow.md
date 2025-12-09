# httpflow

> HTTP 스트림을 캡처하고 덤프하는 커멘드라인 유틸리티.
> 더 많은 정보: <https://github.com/six-ddc/httpflow>.

- 모든 인터페이스에서 트래픽 캡처:

`httpflow -i {{any}}`

- bpf-스타일 캡처를 사용하여 결과를 필터링:

`httpflow {{host httpbin.org 또는 host baidu.com}}`

- 정규식을 사용하여 URL별로 요청을 필터링:

`httpflow -u '{{정규_표현식}}'`

- PCAP 형식 바이너리 파일에서 패킷을 읽음:

`httpflow -r {{out.cap}}`

- 출력을 디렉터리에 씀:

`httpflow -w {{경로/대상/디렉터리}}`
