# darwin-rebuild

> Nix 기반 Darwin (macOS) 시스템 구성을 재빌드하고 전환하는 도구.
> 더 많은 정보: <https://github.com/nix-darwin/nix-darwin>.

- 지정한 Darwin 구성으로 재빌드 후 전환:

`darwin-rebuild switch --flake {{경로/대상/flake}}`

- 구성을 빌드만 하고 전환하지 않음:

`darwin-rebuild build --flake {{경로/대상/flake}}`

- 도움말 표시:

`darwin-rebuild --help`
