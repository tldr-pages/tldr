# genie

> WSL(Windows Subsystem for Linux)에서 systemd를 실행하기 위해 "bottle" 네임스페이스를 설정하고 사용합니다.
> 이미 실행 중인 배포판이 아닌 Windows에서 이를 실행하려면 `wsl`을 앞에 붙입니다.
> 더 많은 정보: <https://github.com/arkane-systems/genie>.

- 보틀 초기화 (시작 시 한 번 실행):

`genie -i`

- 보틀 내부에서 로그인 셸 실행:

`genie -s`

- 보틀 내부에서 특정 명령 실행:

`genie -c {{명령}}`
