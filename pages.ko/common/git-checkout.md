# git checkout

> 브랜치 또는 작업 트리로 경로를 체크아웃합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-checkout>.

- 새로운 브랜치를 생성하고 체크아웃:

`git checkout -b {{브랜치_이름}}`

- 특정 참조를 기반으로 새로운 브랜치를 생성하고 체크아웃 (브랜치, remote/branch, tag가 유효한 참조 예시입니다):

`git checkout -b {{브랜치_이름}} {{참조}}`

- 기존 로컬 브랜치로 체크아웃:

`git checkout {{브랜치_이름}}`

- 이전에 체크아웃한 브랜치로 체크아웃:

`git checkout -`

- 기존 원격 브랜치로 체크아웃:

`git checkout --track {{원격_이름}}/{{브랜치_이름}}`

- 현재 디렉토리에서 모든 스테이징되지 않은 변경 사항을 삭제 (더 많은 취소 유사 명령은 `git reset`을 참조하십시오):

`git checkout .`

- 특정 파일의 스테이징되지 않은 변경 사항 삭제:

`git checkout {{경로/대상/파일}}`

- 현재 디렉토리에 있는 파일을 주어진 브랜치에서 커밋된 버전으로 대체:

`git checkout {{브랜치_이름}} -- {{경로/대상/파일}}`
