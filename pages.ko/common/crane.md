# crane

> 컨테이너 이미지 관리 도구.
> `pull`, `push`, `copy` 등과 같은 일부 하위 명령에는 자체 사용 설명서가 있음.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- `crane` 하위 명령을 실행:

`crane {{하위명령어}}`

- 배포할 수 없는 (외부) 레이어 푸시를 허용:

`crane --allow-nondistributable-artifacts {{하위명령어}}`

- TLS 없이 이미지 참조를 가져오록 허용:

`crane --insecure {{하위명령어}}`

- os/arch{{/variant}}{{:osversion}} 형식으로 플랫폼을 지정 (e.g. linux/amd64). (기본값 모두):

`crane --platform {{플랫폼}} {{하위명령어}}`

- 하위 명령에 대한 디버그 로그 활성화:

`crane {{[-v|--verbose]}} {{하위명령어}}`

- 하위 명령에 대한 도움말 표시:

`crane {{[-h|--help]}} {{하위명령어}}`
