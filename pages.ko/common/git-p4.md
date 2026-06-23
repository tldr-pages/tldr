# git p4

> Perforce 저장소로부터 가져오기 및 제출 수행.
> 더 많은 정보: <https://git-scm.com/docs/git-p4>.

- Perforce depot을 새로운 Git 저장소로 clone:

`git p4 clone {{경로/대상/p4_depot}}`

- 현재 Git 저장소에 Perforce 변경 사항 동기화:

`git p4 sync {{경로/대상/p4_depot}}`

- 최신 Perforce 변경 사항 위에 로컬 커밋 rebase:

`git p4 rebase`

- Git 변경 사항을 Perforce로 다시 제출:

`git p4 submit`

- 최신 changelist만이 아니라 전체 Perforce 히스토리 clone:

`git p4 clone {{경로/대상/p4_depot}}@all`
