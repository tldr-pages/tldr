# nh home

> Nix를 사용하여 사용자별 환경 관리 및 설정.
> `home-manager`를 재구현한 도구.
> 더 많은 정보: <https://github.com/nix-community/nh#usage>.

- 지정한 Home Manager flake 설정을 빌드하고 적용:

`nh home switch {{경로/대상/flake}}`

- 지정한 Home Manager flake의 모든 입력을 업데이트한 후 빌드:

`nh home build {{경로/대상/flake}} {{[-u|--update]}}`

- 지정한 Home Manager flake를 Nix REPL (Nix 평가 환경)에 로드:

`nh home repl {{경로/대상/flake}}`
