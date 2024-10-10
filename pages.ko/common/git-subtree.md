# git subtree

> 프로젝트 종속성을 하위 프로젝트로 관리.
> 더 많은 정보: <https://manpages.debian.org/latest/git-man/git-subtree.1.html>.

- Git 저장소를 서브트리로 추가:

`git subtree add --prefix={{경로/대상/폴더/}} --squash {{repository_url}} {{branch_name}}`

- 서브트리 저장소를 최신 커밋으로 업데이트:

`git subtree pull --prefix={{경로/대상/폴더/}} {{repository_url}} {{branch_name}}`

- 최신 서브트리 커밋까지의 최근 변경 사항을 서브트리에 병합:

`git subtree merge --prefix={{경로/대상/폴더/}} --squash {{repository_url}} {{branch_name}}`

- 커밋을 서브트리 저장소로 푸시:

`git subtree push --prefix={{경로/대상/폴더/}} {{repository_url}} {{branch_name}}`

- 서브트리의 기록에서 새로운 프로젝트 기록 추출:

`git subtree split --prefix={{경로/대상/폴더/}} {{repository_url}} -b {{branch_name}}`
