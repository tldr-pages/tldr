# nix flake

> Nix 플레이크 관리.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-flake.html>.

- 현재 디렉토리에서 기본 템플릿으로 새로운 플레이크(`flake.nix` 파일만) 생성:

`nix flake init`

- 현재 디렉토리의 플레이크의 모든 입력(의존성) 업데이트:

`nix flake update`

- 현재 디렉토리의 플레이크의 특정 입력(의존성) 업데이트:

`nix flake update {{입력}}`

- GitHub에 있는 플레이크의 모든 출력 표시:

`nix flake show {{github:소유자/레포}}`

- 도움말 표시:

`nix flake --help`
