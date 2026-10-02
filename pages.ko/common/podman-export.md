# podman export

> 컨테이너의 파일 시스템을 내보내 로컬 시스템에 tarball로 저장.
> 관련 항목: `podman import`, `podman save`.
> 더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-export.1.html>.

- 컨테이너의 파일 시스템을 `.tar` 파일로 내보내기:

`podman export {{[-o|--output]}} {{경로/대상/파일.tar}} {{컨테이너_이름_또는_아이디}}`

- 컨테이너의 파일 시스템을 `stdout`으로 출력하여 tarball로 저장:

`podman export {{컨테이너_이름_또는_아이디}} > {{경로/대상/파일.tar}}`
