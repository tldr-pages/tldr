# git checkout-index

> 색인에서 작업 트리로 파일 복사.
> 더 많은 정보: <https://git-scm.com/docs/git-checkout-index>.

- 마지막 커밋 이후 삭제된 파일 복원:

`git checkout-index --all`

- 마지막 커밋 이후 삭제되거나 변경된 파일 복원:

`git checkout-index --all --force`

- 마지막 커밋 이후 변경된 파일 복원, 삭제된 파일은 무시:

`git checkout-index --all --force --no-create`

- 마지막 커밋 시점의 전체 트리 복사본을 지정된 디렉토리에 내보내기 (끝의 슬래시가 중요):

`git checkout-index --all --force --prefix={{경로/대상/내보내기_폴더/}}`
