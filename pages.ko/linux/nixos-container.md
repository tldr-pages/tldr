# nixos-container

> Linux 컨테이너를 사용하여 NixOS 컨테이너 시작.
> 더 많은 정보: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- 실행 중인 컨테이너 나열:

`sudo nixos-container list`

- 특정 구성 파일로 NixOS 컨테이너 생성:

`sudo nixos-container create {{컨테이너_이름}} --config-file {{nix_구성_파일_경로}}`

- 특정 컨테이너 시작, 중지, 종료, 또는 삭제:

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{컨테이너_이름}}`

- 실행 중인 컨테이너에서 명령어 실행:

`sudo nixos-container run {{컨테이너_이름}} -- {{명령어}} {{명령어_인자들}}`

- 컨테이너 구성 업데이트:

`sudo $EDITOR /var/lib/container/{{컨테이너_이름}}/etc/nixos/configuration.nix && sudo nixos-container update {{컨테이너_이름}}`

- 이미 실행 중인 컨테이너에 대한 대화형 셸 세션 시작:

`sudo nixos-container root-login {{컨테이너_이름}}`
