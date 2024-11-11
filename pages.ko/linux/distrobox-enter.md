# distrobox-enter

> Distrobox 컨테이너에 진입합니다. 같이 보기: `tldr distrobox`.
> 기본 실행 명령어는 사용자의 SHELL이지만, 다른 셸 또는 전체 명령어를 지정하여 실행할 수 있습니다. 스크립트, 애플리케이션 또는 서비스 내에서 사용 시, `--headless` 모드를 사용하여 tty 및 상호작용을 비활성화할 수 있습니다.
> 더 많은 정보: <https://distrobox.it/usage/distrobox-enter>.

- Distrobox 컨테이너에 진입:

`distrobox-enter {{컨테이너_이름}}`

- Distrobox 컨테이너에 진입하고 로그인 시 명령어 실행:

`distrobox-enter {{컨테이너_이름}} -- {{sh -l}}`

- tty를 인스턴스화하지 않고 Distrobox 컨테이너에 진입:

`distrobox-enter --name {{컨테이너_이름}} -- {{uptime -p}}`
