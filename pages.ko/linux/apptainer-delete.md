# apptainer delete

> 원격 라이브러리에서 컨테이너 이미지를 삭제하는 명령어.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_delete.html>.

- Container Library에서 이미지 삭제:

`apptainer delete library://{{user/collection/container}}:{{태그}}`

- 특정 아키텍처의 이미지 삭제:

`apptainer delete {{[-A|--arch]}} {{amd64|arm64|ppc64le}} library://{{user/collection/container}}:{{태그}}`

- 확인 없이 이미지 강제 삭제:

`apptainer delete {{[-F|--force]}} library://{{user/collection/container}}:{{태그}}`

- 특정 라이브러리 서버에서 이미지 삭제:

`apptainer delete --library {{https://library.example.com}} library://{{user/collection/container}}:{{태그}}`

- HTTPS 대신 HTTP를 사용하여 이미지 삭제:

`apptainer delete --no-https library://{{hostname/user/collection/container}}:{{태그}}`

- 도움말 표시:

`apptainer delete {{[-h|--help]}}`
