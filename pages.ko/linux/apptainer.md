# apptainer

> HPC 및 과학 컴퓨팅을 위한 컨테이너를 관리하는 도구.
> 일부 하위 명령어(`build`, `pull`, `push`)는 별도의 사용법 문서를 가짐.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli.html>.

- Docker Hub에서 컨테이너 다운로드:

`apptainer pull {{경로/대상/이미지.sif}} docker://{{이미지}}:{{태그}}`

- Container Library에서 컨테이너 다운로드:

`apptainer pull {{경로/대상/이미지.sif}} library://{{user/collection/container}}:{{태그}}`

- 정의 파일로부터 컨테이너 빌드:

`apptainer build {{경로/대상/이미지.sif}} {{경로/대상/정의파일.def}}`

- 컨테이너 내부에서 대화형 쉘 실행:

`apptainer shell {{경로/대상/이미지.sif}}`

- 컨테이너 내부에서 명령 실행:

`apptainer exec {{경로/대상/이미지.sif}} {{명령어}}`

- 컨테이너의 기본 runscript 실행:

`apptainer run {{경로/대상/이미지.sif}}`

- 컨테이너 메타데이터 확인:

`apptainer inspect {{경로/대상/이미지.sif}}`

- 도움말 표시:

`apptainer {{[-h|--help]}}`
