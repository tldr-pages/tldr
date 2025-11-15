# nix-env

> Nix 사용자 환경을 조작하거나 조회합니다.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- 설치된 모든 패키지 나열:

`nix-env -q`

- 설치된 패키지 조회:

`nix-env -q {{검색어}}`

- 사용 가능한 패키지 조회:

`nix-env -qa {{검색어}}`

- 패키지 설치:

`nix-env -iA nixpkgs.{{패키지_이름}}`

- URL에서 패키지 설치:

`nix-env -i {{패키지_이름}} --file {{example.com}}`

- 패키지 제거:

`nix-env -e {{패키지_이름}}`

- 특정 패키지 업그레이드:

`nix-env -u {{패키지_이름}}`

- 모든 패키지 업그레이드:

`nix-env -u`
