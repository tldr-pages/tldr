# standard-version

> SemVer 및 Conventional Commits를 사용하여 버전 관리 및 변경 로그 생성을 자동화.
> 더 많은 정보: <https://github.com/conventional-changelog/standard-version>.

- 변경 로그 파일을 업데이트하고 릴리스를 태그 지정:

`standard-version`

- 버전을 올리지 않고 릴리스를 태그 지정:

`standard-version --first-release`

- 변경 로그를 업데이트하고 알파 릴리스를 태그 지정:

`standard-version --prerelease alpha`

- 변경 로그를 업데이트하고 특정 릴리스 유형을 태그 지정:

`standard-version --release-as {{major|minor|patch}}`

- 커밋 단계에서 훅 검증 없이 릴리스를 태그 지정:

`standard-version --no-verify`

- `standard-version`에 의해 영향을 받는 파일뿐만 아니라 모든 스테이징된 변경 사항을 커밋하면서 릴리스를 태그 지정:

`standard-version --commit-all`

- 특정 변경 로그 파일을 업데이트하고 릴리스를 태그 지정:

`standard-version --infile {{경로/대상/파일.md}}`

- 실제로 수행하지 않고 수행될 릴리스를 표시:

`standard-version --dry-run`
