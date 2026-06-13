# bleachbit

> 파일 시스템의 불필요한 파일을 정리합니다.
> 더 많은 정보: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Bleachbit의 그래픽 사용자 인터페이스(GUI) 버전 시작:

`bleachbit --gui`

- 파일 삭제:

`bleachbit --shred {{경로/대상/파일}}`

- 사용 가능한 클리너 옵션 나열:

`bleachbit --list-cleaners`

- 정리 작업을 실제로 수행하기 전에 삭제될 파일 및 변경 사항 미리 보기:

`bleachbit --preview {{--preset|cleaner1.option1 cleaner2.* ...}}`

- 정리 작업 수행 및 파일 삭제:

`bleachbit --clean {{--preset|cleaner1.option1 cleaner2.* ...}}`
