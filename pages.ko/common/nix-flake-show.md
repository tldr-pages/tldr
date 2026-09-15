# nix flake show

> flake가 제공하는 출력을 표시.
> 더 많은 정보: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake-show.html>.

- 현재 디렉터리의 flake 출력 모두 표시:

`nix flake show`

- GitHub의 flake 출력 모두를 한 줄 json으로 표시:

`nix flake show {{github:소유자/저장소}} --json --no-pretty`

- GitHub의 flake `legacyPackages` 출력 모두를 들여쓰기된 여러 줄 json으로 표시:

`nix flake show {{github:소유자/저장소}} --json --pretty --legacy`

- `nix flake init`에서 사용할 수 있는 모든 flake 템플릿 목록 표시:

`nix flake show templates`
