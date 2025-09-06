# nix-build

> Nix 표현식을 빌드.
> 같이 보기: `nix build.3`.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/nix-build.html>.

- Nix 표현식 빌드:

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}}`

- 샌드박스된 Nix 표현식 빌드 (NixOS가 아닌 경우):

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}} --option sandbox true`
