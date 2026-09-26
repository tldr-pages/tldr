# jj file chmod

> `jj` 저장소의 경로에 실행 권한 비트를 설정하거나 제거.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-chmod>.

- 작업 복사본의 파일에 실행 권한 설정:

`jj file chmod {{[x|executable]}} {{경로/대상/파일}}`

- 작업 복사본의 파일에서 실행 권한 제거  (일반 파일로 설정):

`jj file chmod {{[n|normal]}} {{경로/대상/파일}}`

- 여러 파일에 실행 권한 설정:

`jj file chmod {{[x|executable]}} {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 지정한 리비전의 파일에 실행 권한 설정:

`jj file chmod {{[-r|--revision]}} {{revision}} {{[x|executable]}} {{경로/대상/파일}}`
