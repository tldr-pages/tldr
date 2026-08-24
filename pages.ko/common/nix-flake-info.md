# nix flake info

> flake 메타데이터를 표시.
> 더 많은 정보: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake-info>.

- 현재 디렉터리의 flake 메타데이터 표시:

`nix flake info`

- GitHub의 Flake 메타데이터를 한 줄 JSON으로 표시:

`nix flake info {{github:소유자/저장소}} --json --no-pretty`

- Github의 Flake 메타데이터를 들여쓰기된 여러 줄 JSON으로 표시:

`nix flake info {{github:소유자/저장소}} --json --pretty`
