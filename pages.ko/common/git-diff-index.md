# git diff-index

> 작업 디렉터리를 커밋 또는 트리 객체와 비교.
> 더 많은 정보: <https://git-scm.com/docs/git-diff-index>.

- 작업 디렉터리를 특정 커밋과 비교:

`git diff-index {{commit}}`

- 작업 디렉터리 내 특정 파일 또는 폴더를 커밋과 비교:

`git diff-index {{commit}} {{경로/대상/파일_또는_폴더}}`

- 인덱스(스테이징 영역)에 있는 작업 디렉터리를 비교하여 스테이징된 변경 사항 확인:

`git diff-index --cached {{commit}}`

- 출력 억제 및 종료 상태를 반환하여 차이점 확인:

`git diff-index --quiet {{commit}}`
