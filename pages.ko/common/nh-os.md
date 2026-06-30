# nh os

> NixOS 시스템 재구성 및 디버깅.
> 더 많은 정보: <https://github.com/nix-community/nh#usage>.

- 지정한 NixOS flake 설정을 빌드하고 즉시 적용:

`nh os switch {{경로/대상/flake}}`

- 지정한 NixOS flake의 모든 입력을 업데이트하고 빌드한 뒤, 다음 부팅의 기본 설정으로 등록:

`nh os boot {{경로/대상/flake}} {{[-u|--update]}}`

- 지정한 NixOS Flake의 특정 특수 구성(Specialisation)을 빌드하고 활성화:

`nh os test {{경로/대상/flake}} {{[-s|--specialisation]}} {{특수_구성}}`

- 지정한 NixOS flake 호스트를 빌드하고, 결과를 현재 디렉터리에 Nix Store의 심볼릭 링크로 생성:

`nh os build-vm {{경로/대상/flake}} {{[-H|--hostname]}} {{호스트}}`

- 지정한 NixOS flake 설정을 Nix REPL(Nix 평가 환경)에 로드:

`nh os repl {{경로/대상/flake}}`

- 현재 프로필의 모든 세대 목록 표시:

`nh os info`

- 지정한 세대로 롤백:

`nh os rollback {{[-t|-to]}} {{세대}}`
