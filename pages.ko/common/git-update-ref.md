# git update-ref

> Git 참조를 생성, 업데이트 및 삭제하는 Git 명령어.
> 더 많은 정보: <https://git-scm.com/docs/git-update-ref>.

- 참조 삭제 (첫 커밋을 소프트 리셋하는 데 유용):

`git update-ref -d {{HEAD}}`

- 메시지와 함께 참조 업데이트:

`git update-ref -m {{메시지}} {{HEAD}} {{4e95e05}}`
