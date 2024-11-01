# nix classic

> 안정적이고 강력한 패키지 관리자를 위한 클래식하고 안정적인 인터페이스로, 패키지 관리를 신뢰성 있고 재현 가능하며 선언적으로 만듭니다.
> `nix-build`, `nix-shell`, `nix-env`, `nix-store`와 같은 일부 Nix 명령에는 자체 페이지가 있습니다. 같이 보기: `tldr nix`.
> 더 많은 정보: <https://nixos.org>.

- nixpkgs에서 이름으로 패키지 검색:

`nix-env -qaP {{검색_용어_정규식}}`

- 지정된 패키지를 사용 가능한 상태로 쉘 시작:

`nix-shell -p {{패키지1 패키지2 패키지3...}}`

- 일부 패키지를 영구적으로 설치:

`nix-env -iA {{nixpkgs.패키지1 nixpkgs.패키지2...}}`

- 저장소 경로(패키지)의 모든 종속성을 트리 형식으로 표시:

`nix-store --query --tree {{/nix/store/...}}`

- 채널(저장소) 업데이트:

`nix-channel --update`

- Nix 저장소에서 사용하지 않는 경로 제거:

`nix-collect-garbage`
