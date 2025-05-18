# nix edit

> Nix 패키지의 Nix 표현을 $EDITOR에서 엽니다.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-edit.html>.

- nixpkgs에서 패키지의 Nix 표현 소스를 `$EDITOR`에서 열기:

`nix edit {{nixpkgs#패키지}}`

- 패키지의 소스를 `stdout`으로 덤프:

`EDITOR=cat nix edit {{nixpkgs#패키지}}`
