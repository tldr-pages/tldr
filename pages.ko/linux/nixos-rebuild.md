# nixos-rebuild

> NixOS 머신을 재구성합니다.
> 더 많은 정보: <https://nixos.org/nixos/manual/#sec-changing-config>.

- 새로운 설정을 빌드하고 전환하며, 부팅 기본값으로 설정:

`sudo nixos-rebuild switch`

- 새로운 설정을 빌드하고 전환하며, 부팅 기본값으로 설정하고 부팅 항목 이름 지정:

`sudo nixos-rebuild switch {{[-p|--profile-name]}} {{이름}}`

- 새로운 설정을 빌드하고 전환하며, 부팅 기본값으로 설정하고 업데이트 설치:

`sudo nixos-rebuild switch --upgrade`

- 설정 변경 사항을 롤백하고 이전 세대로 전환:

`sudo nixos-rebuild switch --rollback`

- 새로운 설정을 빌드하여 부팅 기본값으로 설정하지만, 전환하지 않음:

`sudo nixos-rebuild boot`

- 새로운 설정을 빌드하고 활성화하지만, 부팅 항목을 만들지 않음 (테스트 용도):

`sudo nixos-rebuild test`

- 설정을 빌드하고 가상 머신에서 열기:

`sudo nixos-rebuild build-vm`

- 부트로더 메뉴에서와 같이 사용 가능한 세대를 나열합니다:

`nixos-rebuild list-generations`
