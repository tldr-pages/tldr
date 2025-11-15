# dvc checkout

> 캐시에서 데이터 파일 및 디렉토리를 체크아웃.
> 더 많은 정보: <https://dvc.org/doc/command-reference/checkout>.

- 모든 대상 파일 및 디렉토리의 최신 버전 체크아웃:

`dvc checkout`

- 지정된 대상의 최신 버전 체크아웃:

`dvc checkout {{대상}}`

- 다른 Git 커밋/태그/브랜치에서 특정 버전의 대상 체크아웃:

`git checkout {{커밋_해시|태그|브랜치}} {{대상}} && dvc checkout {{대상}}`
