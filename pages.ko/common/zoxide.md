# zoxide

> 가장 자주 사용되는 디렉터리를 추적.
> 순위 알고리즘을 사용하여 가장 적합한 경로로 이동.
> 더 많은 정보: <https://github.com/ajeetdsouza/zoxide>.

- 이름에 "foo"가 포함된 가장 높은 순위의 디렉터리로 이동:

`zoxide query {{foo}}`

- 이름에 "foo"와 "bar"가 차례로 포함된 가장 높은 순위의 디렉터리로 이동:

`zoxide query {{foo}} {{bar}}`

- 대화형 디렉터리 검색 시작 (`fzf` 필요):

`zoxide query --interactive`

- 디렉터리를 추가하거나 순위를 증가:

`zoxide add {{경로/대상/폴더}}`

- `zoxide` 데이터베이스에서 디렉터리 제거:

`zoxide remove {{경로/대상/폴더}}`

- 명령 별칭 (`z`, `za`, `zi`, `zq`, `zr`)에 대한 쉘 구성 생성:

`zoxide init {{bash|fish|zsh}}`
