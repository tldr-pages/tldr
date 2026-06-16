# git fast-export

> Git 저장소의 내용과 히스토리를 스트리밍 가능한 일반 텍스트 형식으로 내보내기.
> 더 많은 정보: <https://manned.org/git-fast-export>.

- 전체 Git 저장소 히스토리를 `stdout`으로 출력:

`git fast-export --all`

- 전체 저장소를 파일로 내보내기:

`git fast-export --all > {{경로/대상/파일}}`

- 특정 브랜치만 내보내기:

`git fast-export {{main}}`

- `n`개 객체마다 진행 상태(`progress`) 출력하며 내보내기 (`git fast-import` 진행 표시용):

`git fast-export --progress {{n}} --all > {{경로/대상/파일}}`

- 특정 하위 디렉터리의 히스토리만 내보내기:

`git fast-export --all -- {{경로/대상/디렉토리}} > {{경로/대상/파일}}`
