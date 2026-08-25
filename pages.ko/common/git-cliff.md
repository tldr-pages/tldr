# git cliff

> 매우 높은 수준으로 사용자 지정 가능한 changelog 생성기.
> 더 많은 정보: <https://git-cliff.org/docs/usage/args/>.

- Git 저장소의 모든 커밋으로부터 changelog 생성 후 `CHANGELOG.md`에 저장:

`git cliff > {{CHANGELOG.md}}`

- 최신 태그 이후의 커밋으로 changelog 생성 후 `stdout`에 출력:

`git cliff {{[-l|--latest]}}`

- 현재 태그에 속한 커밋으로 changelog 생성 (`git checkout`으로 태그 상태여야 함):

`git cliff --current`

- 태그에 속하지 않은 커밋으로 changelog 생성:

`git cliff {{[-u|--unreleased]}}`

- 현재 디렉터리에 기본 설정 파일 `cliff.toml` 생성:

`git cliff {{[-i|--init]}}`
