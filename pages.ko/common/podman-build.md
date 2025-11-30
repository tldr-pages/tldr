# podman build

> 컨테이너 이미지를 빌드하기 위한 데몬리스 도구.
> 더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- 지정된 디렉토리의 `Dockerfile` 또는 `Containerfile`을 사용하여 이미지 생성:

`podman build {{경로/대상/폴더}}`

- 지정된 태그로 이미지 생성:

`podman build {{[-t|--tag]}} {{이미지_이름:버전}} {{경로/대상/폴더}}`

- 비표준 파일에서 이미지 생성:

`podman build {{[-f|--file]}} {{Containerfile.different}} .`

- 이전에 캐시된 이미지를 사용하지 않고 이미지 생성:

`podman build --no-cache {{경로/대상/폴더}}`

- 모든 출력을 억제하여 이미지 생성:

`podman build {{[-q|--quiet]}} {{경로/대상/폴더}}`
