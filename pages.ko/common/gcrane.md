# gcrane

> 컨테이너 이미지 관리.
> 이 도구는 `gcr.io`와 관련된 추가 명령과 함께 `crane` 명령의 상위 집합을 구현.
> `append`, `auth`, `copy` 등과 같은 일부 하위 명령에는 `crane` 아래에서 찾을 수 있는 자체 사용법 문서가 존재.
> `completion`, `gc`, `help`와 같은 일부 하위 명령은 gcrane에만 해당되며 자체 사용 문서가 있음.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- `gcrane` 하위 명령을 실행:

`gcrane {{하위명령어}}`

- 배포할 수 없는 (외부) 레이어 푸시를 허용:

`gcrane --allow-nondistributable-artifacts {{하위명령어}}`

- TLS 없이 이미지 참조를 가져오도록 허용:

`gcrane --insecure {{하위명령어}}`

- os/arch{{/variant}}{{:osversion}} 형식으로 플랫폼을 지정 (예: linux/amd64). (기본값은 모두):

`gcrane --platform {{플랫폼}} {{하위명령어}}`

- 디버그 로그 활성화:

`gcrane {{[-v|--verbose]}} {{하위명령어}}`

- 도움말 표시:

`gcrane {{[-h|--help]}}`
