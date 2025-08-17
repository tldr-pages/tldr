# git am

> 패치 파일을 적용하고 커밋 생성. 이메일을 통해 커밋을 받을 때 유용합니다.
> 패치 파일을 생성할 수 있는 `git format-patch`도 같이 보세요.
> 더 많은 정보: <https://git-scm.com/docs/git-am>.

- 로컬 패치 파일을 적용하고 커밋:

`git am {{경로/대상/파일.patch}}`

- 원격 패치 파일을 적용하고 커밋:

`curl {{[-L|--location]}} {{https://example.com/file.patch}} | git apply`

- 패치 파일 적용 과정 중단:

`git am --abort`

- 가능한 한 많은 패치 파일을 적용하고, 실패한 부분을 거부 파일로 저장:

`git am --reject {{경로/대상/파일.patch}}`
