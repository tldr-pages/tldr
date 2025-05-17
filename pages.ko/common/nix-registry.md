# nix registry

> Nix 플레이크 레지스트리를 관리.
> 같이 보기: 플레이크에 대한 정보는 `nix flake`.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-registry.html>.

- `nixpkgs` 리비전을 업스트림 저장소의 현재 버전으로 고정:

`nix registry pin {{nixpkgs}}`

- GitHub 저장소의 최신 버전 브랜치 또는 특정 리비전으로 항목 고정:

`nix registry pin {{항목}} {{github:소유자/레포/브랜치_또는_리비전}}`

- GitHub 저장소의 최신 버전을 항상 가리키며 자동으로 업데이트되는 새 항목 추가:

`nix registry add {{항목}} {{github:소유자/레포}}`

- 레지스트리 항목 제거:

`nix registry remove {{항목}}`

- Nix 플레이크 레지스트리가 무엇인지에 대한 문서 보기:

`nix registry --help`
