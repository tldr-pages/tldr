# apptainer registry

> OCI/Docker 레지스트리에 대한 인증을 관리하는 도구.
> 관련 항목: `apptainer pull`, `apptainer push`.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_registry.html>.

- 설정된 모든 레지스트리 자격 증명 목록 출력:

`apptainer registry list`

- 사용자 이름으로 레지스트리에 로그인 (password will be prompted):

`apptainer registry login {{[-u|--username]}} {{사용자명}} docker://{{레지스트리}}`

- 사용자 정의 OCI 레지스트리에 로그인:

`apptainer registry login {{[-u|--username]}} {{사용자명}} oras://{{레지스트리}}`

- 사용자 이름과 비밀번호로 로그인:

`apptainer registry login {{[-u|--username]}} {{사용자명}} {{[-p|--password]}} {{password}} docker://{{레지스트리}}`

- `stdin`으로 비밀번호를 전달하여 로그인:

`echo "{{password}}" | apptainer registry login {{[-u|--username]}} {{사용자명}} --password-stdin docker://{{레지스트리}}`

- 사용자 정의 인증 파일을 사용하여 로그인:

`apptainer registry login --authfile {{path/to/auth.json}} {{[-u|--username]}} {{사용자명}} docker://{{레지스트리}}`

- 레지스트리에서 로그아웃:

`apptainer registry logout docker://{{레지스트리}}`

- 사용자 정의 인증 파일을 사용하여 로그아웃:

`apptainer registry logout --authfile {{path/to/auth.json}} docker://{{레지스트리}}`
