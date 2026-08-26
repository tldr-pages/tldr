# podman save

> 이미지를 로컬 파일 또는 디렉터리에 저장.
> 관련 항목: `podman load`, `podman export`.
> 더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-save.1.html>.

- 이미지를 `.tar` 파일로 저장:

`podman save {{[-o|--output]}} {{경로/대상/파일.tar}} {{이미지:태그}}`

- 이미지를 `stdout`으로 출력하여 저장:

`podman save {{이미지:태그}} > {{경로/대상/파일.tar}}`

- 이미지를 압축하여 저장:

`podman save {{이미지:태그}} | {{[gzip|bzip2|xz|zstd|zstdchunked]}} > {{경로/대상/파일.tar[.gz|.bz2|.xz|.zst|.zst]}}`

- 이미지를 실시간으로 압축하며 진행률을 표시하고 원격 시스템으로 전송:

`podman save {{이미지:태그}} | zstd {{[-T|--threads]}} 0 --ultra | pv | ssh {{사용자명}}@{{원격_호스트}} podman load`
