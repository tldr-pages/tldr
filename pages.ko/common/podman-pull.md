# podman pull

> 컨테이너 레지스트리에서 이미지를 가져오기.
> 더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-pull.1.html>.

- 지정한 컨테이너 이미지 가져오기:

`podman pull {{이미지}}:{{tag}}`

- 조용한 모드로 컨테이너 이미지 가져오기:

`podman pull {{[-q|--quiet]}} {{이미지}}:{{태그}}`

- 컨테이너 이미지의 모든 태그 가져오기:

`podman pull {{[-a|--all-tags]}} {{이미지}}`

- 지정한 플랫폼용 컨테이너 이미지 가져오기:

`podman pull --platform {{linux/arm64}} {{이미지}}:{{tag}}`

- TLS 검증 없이 컨테이너 이미지 가져오기:

`podman pull --tls-verify=false {{이미지}}:{{태그}}`

- 도움말 표시:

`podman pull {{[-h|--help]}}`
