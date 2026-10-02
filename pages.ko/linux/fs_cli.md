# fs_cli

> FreeSWITCH 명령줄 인터페이스 (ESL 클라이언트)를 사용하여 실행중인 FreeSWITCH 서버에 연결하고 제어.
> 더 많은 정보: <https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Client-and-Developer-Interfaces/1048948/>.

- 로컬 FreeSWITCH 인스턴스에 연결하여 대화형 세션 시작:

`fs_cli`

- 원격 FreeSWITCH 서버에 연결:

`fs_cli {{[-H|--host]}} {{호스트}} {{[-P|--port]}} {{port}} {{[-p|--password]}} {{패스워드}}`

- 단일 FreeSWITCH 명령을 실행한 후 종료:

`fs_cli {{[-x|--execute]}} "{{명령어}}"`

- FreeSWITCH 시스템 상태 표시:

`fs_cli {{[-x|--execute]}} "status"`

- FreeSWITCH XML 설정 다시 불러오기:

`fs_cli {{[-x|--execute]}} "reloadxml"`

- 모듈이 로드되어 있는지 확인:

`fs_cli {{[-x|--execute]}} "module_exists {{모듈_이름}}"`

- 현재 활성 통화 목록 표시:

`fs_cli {{[-x|--execute]}} "show calls"`

- 연결 실패 시 재시도:

`fs_cli {{[-r|--retry]}}`
