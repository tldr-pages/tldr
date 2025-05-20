# nix store

> Nix 저장소를 조작.
> 같이 보기: `nix-store`.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-store.html>.

- 가비지 수집을 통해 공간 사용량 줄이기 위해 사용되지 않는 경로 제거:

`nix store gc`

- 동일한 파일을 하드링크하여 공간 사용량 줄이기:

`nix store optimise`

- 특정 저장소 경로 삭제 (사용되지 않아야 함):

`nix store delete {{/nix/store/...}}`

- 원격 저장소의 경로 내용을 나열:

`nix store --store {{https://cache.nixos.org}} ls {{/nix/store/...}}`

- 두 저장소 경로 간의 버전 차이와 해당 종속성 표시:

`nix store diff-closures {{/nix/store/...}} {{/nix/store/...}}`
