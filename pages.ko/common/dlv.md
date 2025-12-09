# dlv

> Go 프로그래밍 언어용 디버거.
> 더 많은 정보: <https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv.md>.

- 현재 디렉터리에서 기본 패키지를 컴파일하고, 디버깅을 시작 (기본으로 인수가 없음):

`dlv debug`

- 특정 패키지를 컴파일하고 디버깅을 시작:

`dlv debug {{패키지}} {{인수}}`

- 테스트 바이너리를 컴파일하고 컴파일된 프로그램 디버깅을 시작:

`dlv test`

- 헤드리스 디버그 서버에 연결:

`dlv connect {{ip_주소}}`

- 실행 중인 프로세스에 연결하고 디버깅을 시작:

`dlv attach {{pid}}`

- 프로그램 컴파일 및 추적 시작:

`dlv trace {{패키지}} --regexp '{{정규_표현식}}'`
