# fuser

> 파일이나 소켓을 현재 사용 중인 프로세스 ID를 표시합니다.
> 더 많은 정보: <https://manned.org/fuser>.

- 파일이나 폴더에 접근 중인 프로세스 찾기:

`fuser {{경로/대상/파일_또는_폴더}}`

- 더 많은 필드 표시 (`USER`, `PID`, `ACCESS`, `COMMAND`):

`fuser --verbose {{경로/대상/파일_또는_폴더}}`

- TCP 소켓을 사용하는 프로세스 식별:

`fuser --namespace tcp {{포트}}`

- 파일이나 폴더에 접근 중인 모든 프로세스 종료 (`SIGKILL` 신호 전송):

`fuser --kill {{경로/대상/파일_또는_폴더}}`

- 특정 파일이나 폴더가 포함된 파일 시스템에 접근 중인 프로세스 찾기:

`fuser --mount {{경로/대상/파일_또는_폴더}}`

- 특정 포트에서 TCP 연결을 가진 모든 프로세스 종료:

`fuser --kill {{포트}}/tcp`
