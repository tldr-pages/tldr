# toolbox run

> 기존 Toolbx 컨테이너에서 명령을 실행합니다.
> 관련 항목: `toolbox enter`.
> 더 많은 정보: <https://manned.org/toolbox-run>.

- 특정 Toolbx 컨테이너 내에서 명령 실행:

`toolbox run {{[-c|--container]}} {{컨테이너_이름}} {{명령}}`

- 특정 배포판 릴리스의 Toolbx 컨테이너 내에서 명령 실행:

`toolbox run {{[-d|--distro]}} {{배포판}} {{[-r|--release]}} {{릴리스}} {{명령}}`

- Fedora 39의 기본 이미지로 Toolbx 컨테이너 내에서 `emacs` 실행:

`toolbox run {{[-d|--distro]}} {{fedora}} {{[-r|--release]}} f{{39}} {{emacs}}`
