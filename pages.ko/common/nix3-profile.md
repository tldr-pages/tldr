# nix profile

> Nix 프로필에서 패키지를 설치, 업데이트 및 제거.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-profile.html>.

- 기본 프로필에 nixpkgs에서 일부 패키지 설치:

`nix profile install {{nixpkgs#패키지1 nixpkgs#패키지2 ...}}`

- GitHub의 플레이크에서 패키지를 사용자 지정 프로필에 설치:

`nix profile install {{github:소유자/레포/패키지}} --profile {{./경로/대상/폴더}}`

- 기본 프로필에 현재 설치된 패키지 나열:

`nix profile list`

- 기본 프로필에서 nixpkgs로 설치된 패키지를 이름으로 제거:

`nix profile remove {{레거시패키지.x86_64-linux.pkg}}`

- 기본 프로필의 패키지를 최신 버전으로 업그레이드:

`nix profile upgrade`

- 기본 프로필에서 최신 작업 롤백(취소):

`nix profile rollback`
