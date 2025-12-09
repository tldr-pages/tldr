# gt

> Git 및 GitHub에 대한 종속 코드 변경(스택) 시퀀스를 생성하고 관리.
> 더 많은 정보: <https://graphite.dev/docs/get-started>.

- Graphite의 API를 사용하여 CLI 인증:

`gt auth --token {{graphite_cli_인증_토큰}}`

- 현재 디렉터리의 저장소에 대해 `gt`를 초기화:

`gt repo init`

- 현재 브랜치 위에 쌓은 새로운 브랜치를 만들고 단계적 변경 사항을 커밋:

`gt branch create {{브랜치_이름}}`

- 새로운 커밋을 생성하고 업스택 브랜치를 수정:

`gt commit create -m {{커밋_메시지}}`

- 현재 스택의 모든 브랜치를 GitHub에 강제로 푸시하고 PR을 생성하거나 업데이트:

`gt stack submit`

- 추적된 모든 스택을 기록:

`gt log short`

- 지정된 하위 명령에 대한 도움말을 표시:

`gt {{하위명령어}} --help`
