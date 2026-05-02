# apptainer test

> Apptainer 컨테이너 이미지에 정의된 테스트 스크립트를 실행하는 도구.
> 테스트 스크립트는 정의 파일의 `%test` 섹션에 작성됨.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_test.html>.

- 컨테이너의 테스트 스크립트 실행:

`apptainer test {{경로/대상/이미지.sif}}`

- 호스트 디렉터리를 컨테이넝 bind 마운트하여 테스트 실행:

`apptainer test {{[-B|--bind]}} {{경로/대상/소스파일}}:{{경로/대상/목적파일}} {{경로/대상/이미지.sif}}`

- 완전 격리 모드에서 테스트 실행 실행 (filesystem, PID, IPC, 환경 분리):

`apptainer test {{[-C|--containall]}} {{경로/대상/이미지.sif}}`

- 쓰기 가능한 임시 파일시스템 오버레이로 테스트 실행:

`apptainer test --writable-tmpfs {{경로/대상/이미지.sif}}`

- 컨테이너 내 특정 애플리케이션의 테스트 스크립트 실행:

`apptainer test --app {{애플리케이션_이름}} {{경로/대상/이미지.sif}}`

- 도움말 표시:

`apptainer test {{[-h|--help]}}`
