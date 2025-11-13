# git annex

> Git을 사용하여 파일을 관리하지만, 파일의 내용을 체크인하지 않습니다.
> 파일이 annexed되면, 해당 내용이 키-값 저장소로 이동되고, 내용을 가리키는 심볼릭 링크가 생성됩니다.
> 더 많은 정보: <https://git-annex.branchable.com/git-annex/>.

- Git annex로 저장소 초기화:

`git annex init`

- 파일 추가:

`git annex add {{경로/대상/파일_또는_폴더}}`

- 파일 또는 디렉토리의 현재 상태 표시:

`git annex status {{경로/대상/파일_또는_폴더}}`

- 로컬 저장소를 원격과 동기화:

`git annex {{원격}}`

- 파일 또는 디렉토리 가져오기:

`git annex get {{경로/대상/파일_또는_폴더}}`

- 도움말 표시:

`git annex help`
