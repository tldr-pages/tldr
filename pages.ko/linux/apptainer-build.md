# apptainer build

> Apptainer 컨테이너 이미지 빌드.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_build.html>.

- 정의 파일로부터 컨테이너 빌드:

`apptainer build {{경로/대상/이미지.sif}} {{경로/대상/정의파일.def}}`

- Docker Hub에서 컨테이너 빌드:

`apptainer build {{경로/대상/이미지.sif}} docker://{{이미지}}:{{태그}}`

- Container Library에서 컨테이너 빌드:

`apptainer build {{경로/대상/이미지.sif}} library://{{user/collection/container}}:{{태그}}`

- Build a writable sandbox directory instead of an image file:

`apptainer build {{[-s|--sandbox]}} {{경로/대상/디렉토리}} docker://{{이미지}}:{{태그}}`

- 캐시를 사용하지 않고 컨테이너 빌드:

`apptainer build --disable-cache {{경로/대상/이미지.sif}} docker://{{이미지}}:{{태그}}`

- 기존 이미지 파일 강제 덮어쓰기:

`apptainer build {{[-F|--force]}} {{경로/대상/이미지.sif}} {{경로/대상/정의파일.def}}`

- 권한이 없는 환경에서 fakeroot를 사용해 빌드:

`apptainer build {{[-f|--fakeroot]}} {{경로/대상/이미지.sif}} {{경로/대상/정의파일.def}}`

- 도움말 표시:

`apptainer build {{[-h|--help]}}`
