# poetry publish

> 패키지를 원격 저장소에 배포.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#publish>.

- 현재 패키지를 PyPI에 배포:

`poetry publish`

- 패키지를 빌드한 후 배포:

`poetry publish --build`

- 지정한 저장소에 패키지 배포:

`poetry publish {{[-r|--repository]}} {{저장소_이름}}`

- 지정한 인증 정보를 사용해 패키지 배포:

`poetry publish {{[-u|--username]}} {{사용자명}} {{[-p|--password]}} {{비밀번호}}`

- 실제 배포 없이 수행될 작업 dry run:

`poetry publish --dry-run`

- 저장소에 이미 존재하는 파일은 건너뛰고 배포:

`poetry publish --skip-existing`
