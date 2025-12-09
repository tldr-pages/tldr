# nix develop

> 파생물의 빌드 환경을 제공하는 Bash 셸 실행.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html>.

- nixpkgs의 모든 {{패키지}} 종속성을 사용하여 셸 시작:

`nix develop {{nixpkgs#pkg}}`

- 현재 디렉토리의 플레이크에 있는 기본 패키지에 대한 개발 셸 시작:

`nix develop`

- 해당 셸에서 소스 구성 및 빌드:

`configurePhase; buildPhase`
