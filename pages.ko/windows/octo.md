# octo

> Octopus Deploy 명령줄 도구.
> 더 많은 정보: <https://octopus.com/docs/octopus-rest-api/octo.exe-command-line>.

- 패키지 생성:

`octo pack --id={{패키지}}`

- 패키지를 Octopus 서버의 저장소에 푸시:

`octo push --package={{패키지}}`

- 릴리스 생성:

`octo create-release --project={{프로젝트_이름}} --packageversion={{버전}}`

- 릴리스 배포:

`octo deploy-release --project={{프로젝트_이름}} --packageversion={{버전}} --deployto={{환경_이름}} --tenant={{배포_대상}}`
