# stat

> 파일 및 파일 시스템 정보를 표시.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- 특정 파일에 대한 속성(크기, 권한, 생성 및 액세스 날짜 등) 표시:

`stat {{경로/대상/파일}}`

- 레이블 없이 특정 파일에 대한 속성(크기, 권한, 생성 및 액세스 날짜 등) 표시:

`stat --terse {{경로/대상/파일}}`

- 특정 파일이 있는 파일 시스템에 대한 정보 표시:

`stat --file-system {{경로/대상/파일}}`

- 8진수 파일 권한만 표시:

`stat --format="%a %n" {{경로/대상/파일}}`

- 특정 파일의 소유자 및 그룹 표시:

`stat --format="%U %G" {{경로/대상/파일}}`

- 특정 파일의 크기를 바이트 단위로 표시:

`stat --format="%s %n" {{경로/대상/파일}}`
