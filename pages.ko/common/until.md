# until

> 종료 상태가 0이 될때까지 반복하는 간단한 쉘 루프.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-until>.

- 명령어 성공할 때까지 반복 실행:

`until {{명령어}}; do :; done`

- SSH 호스트에 연결이 정상적으로 종료될 때까지 연결 시도 반복:

`until ssh {{사용자명}}@{{호스트}}; do sleep {{2}}; done`

- systemd 서비스가 활성 상태가 될 때까지 대기:

`until systemctl is-active {{[-q|--quiet]}} {{nginx}}; do {{echo "Waiting..."}}; sleep 1; done; {{echo "Launched!"}}`
