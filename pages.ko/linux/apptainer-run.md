# apptainer run

> Apptainer 컨테이너의 기본 runscript를 실행하는 명령어.
> runscript는 정의 파일의 `%runscript` 섹션에 정의됨.
> 관련 항목: `apptainer exec`, `apptainer shell`.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_run.html>.

- 컨테이너의 기본 runscript 실행:

`apptainer run {{경로/대상/이미지.sif}}`

- runscript에 인자를 전달하여 실행:

`apptainer run {{경로/대상/이미지.sif}} {{인자1 인자2 ...}}`

- 호스트 디렉터리를 컨테이너에 bind 마운트하여 실행:

`apptainer run {{[-B|--bind]}} {{경로/대상/소스파일}}:{{경로/대상/목적파일}} {{경로/대상/이미지.sif}}`

- 환경 변수를 설정하여 실행:

`apptainer run --env {{변수}}={{값}} {{경로/대상/이미지.sif}}`

- 완전 격리 모드에서 실행 (filesystem, PID, IPC, 환경 분리):

`apptainer run {{[-C|--containall]}} {{경로/대상/이미지.sif}}`

- 쓰기 가능한 임시 파일시스템 오버레이 사용:

`apptainer run --writable-tmpfs {{경로/대상/이미지.sif}}`

- NVIDIA GPU 지원 활성화하여 실행:

`apptainer run --nv {{경로/대상/이미지.sif}}`

- 도움말 표시:

`apptainer run {{[-h|--help]}}`
