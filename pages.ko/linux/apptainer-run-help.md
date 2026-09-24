# apptainer run-help

> Apptainer 컨테이너 이미지에 정의된 사용자 도움말을 출력하는 도구.
> 도움말 내용은 정의 파일의 `%help` 섹션에 작성됨.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_run-help.html>.

- 컨테이너의 도움말 출력:

`apptainer run-help {{경로/대상/이미지.sif}}`

- 컨테이너 내 특정 애플리케이션의 도움말 출력:

`apptainer run-help --app {{애플리케이션_이름}} {{경로/대상/이미지.sif}}`

- 도움말 표시:

`apptainer run-help {{[-h|--help]}}`
