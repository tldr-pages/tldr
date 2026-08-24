# ndc

> 네임서버를 제어하기 위한 name daemon control 서비스.
> 명령을 지정하지 않으면, NDC는 EOF가 올 때까지 입력을 기다림.
> 더 많은 정보: <https://manned.org/ndc>.

- 제어([c]ontrol) 채널 연결 지점 설정:

`ndc -c {{채널}} {{명령어}}`

- 클라이언트 측을 특정 로컬 소켓([l]ocalsock) 주소에 bind:

`ndc -l {{로컬_소켓}} {{명령어}}`

- UNIX 시그널 제어를 위한 pid파일([p]idfile) 경로 설정:

`ndc -p {{경로/대상/pidfile}} {{명령어}}`

- 디버깅([d]ebugging) 모드 활성화:

`ndc -d {{명령어}}`

- 조용한([q]uiet) 모드 활성화:

`ndc -q {{명령어}}`

- 비치명적 오류 억제([s]uppression):

`ndc -s {{명령어}}`

- 프로토콜 및 시스템 디버깅을 위한 트레이싱([t]racing) 활성화:

`ndc -t {{명령어}}`

- 내장 명령 목록 출력:

`ndc /help`
