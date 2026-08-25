# gitea

> 경량 Git 호스팅 서버인 Gitea 관리.
> 설정된 `app.ini` 파일 또는 환경 변수가 필요.
> 더 많은 정보: <https://docs.gitea.com/administration/command-line>.

- 기본 설정으로 Gitea 웹 서버 실행:

`gitea web`

- 필요한 데이터베이스 스키마 및 테이블 생성:

`gitea migrate`

- 사용자 관리 또는 인증 관리용 관리자 하위 명령 실행:

`gitea admin {{user list}}`

- 특정 하위 명령어 도움말 표시:

`gitea {{admin}} --help`

- 도움말 표시:

`gitea help`

- 버전 표시:

`gitea --version`
