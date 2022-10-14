# git am

> 패치 파일을 적용한다. 이메일로 커밋을 받을 때 유용함.
> 패치 파일을 생성 할 수 있는 `git format-patch` 또한 참고.
> 더 많은 정보: <https://git-scm.com/docs/git-am>.

- 패치 파일 적용:

`git am {{경로/대상/파일.patch}}`

- 패치 파일 적용 프로세스 중단:

`git am --abort`

- 가능한 많은 수의 패치 파일 적용, 실패한 파일은 거절 파일에 저장:

`git am --reject {{경로/대상/파일.patch}}`
