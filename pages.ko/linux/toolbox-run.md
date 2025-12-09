# toolbox run

> 기존 `toolbox` 컨테이너에서 명령을 실행합니다.
> 같이 보기: `toolbox enter`.
> 더 많은 정보: <https://manned.org/toolbox-run>.

- 특정 `toolbox` 컨테이너 내에서 명령 실행:

`toolbox run --container {{컨테이너_이름}} {{명령}}`

- 특정 배포판 릴리스의 `toolbox` 컨테이너 내에서 명령 실행:

`toolbox run --distro {{배포판}} --release {{릴리스}} {{명령}}`

- Fedora 39의 기본 이미지로 `toolbox` 컨테이너 내에서 `emacs` 실행:

`toolbox run --distro {{fedora}} --release {{f39}} {{emacs}}`
