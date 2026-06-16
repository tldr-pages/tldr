# apptainer shell

> Apptainer 컨테이너 내부에서 대화형 쉘을 실행하는 명령어.
> 관련 항목: `apptainer exec`, `apptainer run`.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_shell.html>.

- 컨테이너 내부에서 대화형 쉘 실행:

`apptainer shell {{경로/대상/이미지.sif}}`

- 호스트 디렉터리를 컨테이넝 bind 마운트하여 쉘 실행:

`apptainer shell {{[-B|--bind]}} {{경로/대상/소스파일}}:{{경로/대상/목적파일}} {{경로/대상/이미지.sif}}`

- 환경 변수를 설정하여 쉘 실행:

`apptainer shell --env {{변수}}={{값}} {{경로/대상/이미지.sif}}`

- 완전 격리 모드에서 셸 실행 (filesystem, PID, IPC, 환경 분리):

`apptainer shell {{[-C|--containall]}} {{경로/대상/이미지.sif}}`

- 쓰기 가능한 임시 파일시스템 오버레이로 셸 실행:

`apptainer shell --writable-tmpfs {{경로/대상/이미지.sif}}`

- NVIDIA GPU 지원 활성화하여 셸 실행:

`apptainer shell --nv {{경로/대상/이미지.sif}}`

- 특정 셸 프로그램을 사용하여 실행:

`apptainer shell {{[-s|--shell]}} {{path/to/shell}} {{경로/대상/이미지.sif}}`

- 도움말 표시:

`apptainer shell {{[-h|--help]}}`
