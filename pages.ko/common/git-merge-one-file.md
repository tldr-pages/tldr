# git merge-one-file

> 단순 병합 이후 단일 파일 병합 해결.
> 더 많은 정보: <https://git-scm.com/docs/git-merge-one-file>.

- 특정 파일의 단순 병합 충돌 해결:

`git merge-one-file {{경로/대상/파일}}`

- merge-index에서 특정 파일용 헬퍼로 사용:

`git merge-index git-merge-one-file {{경로/대상/파일}}`

- 바이너리 파일 병합 처리:

`git merge-one-file -p {{경로/대상/파일}}`

- 스크립트 기반 병합에서 read-tree 이후 적용:

`git read-tree -m {{브랜치1}} {{브랜치2}} && git merge-index git-merge-one-file {{경로/대상/파일}}`
