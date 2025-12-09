# nix why-depends

> 패키지가 다른 패키지에 의존하는 이유를 보여줍니다.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-why-depends.html>.

- 현재 실행 중인 NixOS 시스템이 특정 저장소 경로를 요구하는 이유를 표시:

`nix why-depends {{/run/현재_시스템}} {{/nix/store/...}}`

- nixpkgs의 패키지가 다른 패키지를 _빌드 타임_ 의존성으로 요구하는 이유를 표시:

`nix why-depends --derivation {{nixpkgs#의존자}} {{nixpkgs#의존성}}`
