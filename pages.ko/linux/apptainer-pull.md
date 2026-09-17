# apptainer pull

> 원격 소스에서 컨테이너 이미지를 다운로드하는 명령어.
> 관련 항목: `apptainer-push`.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_pull.html>.

- Docker Hub에서 컨테이너 다운로드:

`apptainer pull {{경로/대상/이미지.sif}} docker://{{이미지}}:{{태그}}`

- Pull a container from the Container Library에서 컨테이너 다운로드:

`apptainer pull {{경로/대상/이미지.sif}} library://{{user/collection/container}}:{{태그}}`

- OCI 레지스트리에서 컨테이너 다운로드:

`apptainer pull {{경로/대상/이미지.sif}} oras://{{registry/namespace/image}}:{{태그}}`

- 특정 아키텍처용 컨테이너 다운로드:

`apptainer pull --arch {{amd64|arm64|ppc64le}} {{경로/대상/이미지.sif}} library://{{이미지}}:{{태그}}`

- 기존 이미지 파일 강제 덮어쓰기:

`apptainer pull {{[-F|--force]}} {{경로/대상/이미지.sif}} docker://{{이미지}}:{{태그}}`

- 쓰기 가능한 sandbox 디렉터리로 컨테이너 다운로드:

`apptainer pull --sandbox {{경로/대상/디렉터리}} docker://{{이미지}}:{{태그}}`

- 캐시를 사용하지 않고 컨테이너 다운로드:

`apptainer pull --disable-cache {{경로/대상/이미지.sif}} docker://{{이미지}}:{{tag}}`

- 도움말 표시:

`apptainer pull {{[-h|--help]}}`
