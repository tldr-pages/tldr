# nix search

> Nix 플레이크에서 패키지를 검색.
> 같이 보기: 플레이크에 대한 정보는 `nix flake`.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-search.html>.

- `nixpkgs`에서 이름이나 설명을 기반으로 패키지 검색:

`nix search {{nixpkgs}} {{검색_어구...}}`

- nixpkgs에서 패키지 설명 표시:

`nix search {{nixpkgs#패키지}}`

- github에서 플레이크로부터 사용할 수 있는 모든 패키지 표시:

`nix search {{github:소유자/레포}}`
