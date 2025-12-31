# git apply

> 커밋을 생성하지 않고 파일 및/또는 색인에 패치를 적용합니다.
> 같이 보기: `git am` (패치를 적용하고 커밋도 생성).
> 더 많은 정보: <https://git-scm.com/docs/git-apply>.

- 패치된 파일에 대한 메시지 출력:

`git apply {{[-v|--verbose]}} {{경로/대상/파일}}`

- 패치를 적용하고 패치된 파일을 색인에 추가:

`git apply --index {{경로/대상/파일}}`

- 원격 패치 파일 적용:

`curl {{[-L|--location]}} {{https://example.com/file.patch}} | git apply`

- 입력에 대한 diffstat을 출력하고 패치를 적용:

`git apply --stat --apply {{경로/대상/파일}}`

- 패치를 역방향으로 적용:

`git apply {{[-R|--reverse]}} {{경로/대상/파일}}`

- 작업 트리를 수정하지 않고 패치 결과를 색인에 저장:

`git apply --cache {{경로/대상/파일}}`
