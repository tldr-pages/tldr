# homectl

> systemd-homed 서비스를 사용하여 홈 디렉토리를 생성, 제거, 변경 또는 검사합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/homectl.html>.

- 사용자 계정과 관련된 홈 디렉토리 나열:

`homectl list`

- 사용자 계정과 관련된 홈 디렉토리 생성:

`sudo homectl create {{사용자명}}`

- 특정 사용자 및 관련 홈 디렉토리 제거:

`sudo homectl remove {{사용자명}}`

- 특정 사용자의 비밀번호 변경:

`sudo homectl passwd {{사용자명}}`

- 특정 홈 디렉토리에 접근하여 셸 또는 명령 실행:

`sudo homectl with {{사용자명}} -- {{명령}} {{명령_인자}}`

- 특정 홈 디렉토리 잠금 또는 잠금 해제:

`sudo homectl {{lock|unlock}} {{사용자명}}`

- 특정 홈 디렉토리에 할당된 디스크 공간을 100 GiB로 변경:

`sudo homectl resize {{사용자명}} {{100G}}`

- 도움말 표시:

`homectl --help`
