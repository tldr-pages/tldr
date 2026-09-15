# podman load

> `podman save`로 생성한 oci 아카이브 또는 docker 아카이브에서 이미지를 불러옴.
> 관련 항목: `podman save`, `podman import`.
> 더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-load.1.html>.

- `.tar` 파일에서 이미지 불러오기:

`podman load {{[-i|--input]}} {{경로/대상/파일.tar}}`

- 압축된 `.tar` 파일에서 이미지 불러오기:

`podman load {{[-i|--input]}} {{경로/대상/파일.tar[.gz|.bz2|.xz|.zst]}}`

- 이미지를 불러오고 이미지 ID만 출력:

`podman load {{[-q|--quiet]}} {{[-i|--input]}} {{경로/대상/파일.tar}}`

- `stdin`에서 이미지 불러오기:

`podman < {{경로/대상/파일.tar}} load`
