# kmscon

> TTY에서 텍스트 모드 대신 프레임버퍼를 사용하여 터미널을 표시.
> 더 많은 정보: <https://manned.org/kmscon>.

- 사용 가능한 첫 번째 TTY에서 `kmscon` 시작:

`sudo kmscon`

- 지정한 TTY에서 `kmscon` 시작:

`sudo kmscon --vt {{/dev/ttyX|ttyX|X}}`

- 마우스 지원 활성화:

`sudo kmscon --mouse`

- 로그인에 사용할 명령 지정:

`sudo kmscon {{[-l|--login]}} {{명령어}}`

- 지정한 터미널에서 항상 `kmscon` 시작:

`systemctl enable --now kmsconvt@{{ttyX}}`
