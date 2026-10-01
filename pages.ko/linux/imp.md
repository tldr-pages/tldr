# imp

> WSL (Windows Subsystem for Linux)에서 systemd를 기본적으로 사용할 수 있도록 지원하는 도구.
> 참고: 이미 실행중인 배포판이 아닌 Windows에서 실행하려면, 명령 앞에 `wsl`을 붙여야 함.
> 더 많은 정보: <https://github.com/arkane-systems/bottle-imp#usage>.

- 도우미 기능을 초기화하고 명시적으로 종료할 때까지 WSL 실행 유지 (시작 시 한 번만 실행):

`imp {{[-i|--initialize]}}`

- systemd 사용자 세션에서 쉘 실행:

`imp {{[-s|--shell]}}`

- systemd 사용자 세션에서 지정한 명령 실행 (현재 작업 디렉터리 유지):

`imp {{[-c|--command]}} {{명령어}}`

- systemd와 WSL 인스턴스 종료:

`imp {{[-u|--shutdown]}}`
