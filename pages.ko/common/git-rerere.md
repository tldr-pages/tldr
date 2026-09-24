# git rerere

> 병합 충돌 해결 내역 재사용.
> 더 많은 정보: <https://git-scm.com/docs/git-rerere>.

- 전역으로 rerere 활성화:

`git config --global rerere.enabled true`

- 특정 파일의 기록된 충돌 해결 내역 삭제:

`git rerere forget {{경로/대상/파일}}`

- 기록된 충돌 해결 상태 확인:

`git rerere status`
