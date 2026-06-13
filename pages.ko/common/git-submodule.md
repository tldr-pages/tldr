# git submodule

> 서브모듈을 검사하고 업데이트하며 관리합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-submodule>.

- 저장소의 지정된 서브모듈 설치:

`git submodule update --init --recursive`

- Git 저장소를 서브모듈로 추가:

`git submodule add {{repository_url}}`

- Git 저장소를 지정된 폴더에 서브모듈로 추가:

`git submodule add {{repository_url}} {{경로/대상/폴더}}`

- 모든 서브모듈을 최신 커밋으로 업데이트:

`git submodule foreach git pull`
