# readpe

> PE 파일에 대한 정보 표시.
> 더 많은 정보: <https://manned.org/readpe>.

- PE 파일에 대한 모든 정보 표시:

`readpe {{경로/대상/실행파일}}`

- PE 파일에 존재하는 모든 헤더 표시:

`readpe --all-headers {{경로/대상/실행파일}}`

- PE 파일에 존재하는 모든 섹션 표시:

`readpe --all-sections {{경로/대상/실행파일}}`

- PE 파일에서 특정 헤더 표시:

`readpe --header {{dos|coff|optional}} {{경로/대상/실행파일}}`

- 가져온 모든 함수 나열:

`readpe --imports {{경로/대상/실행파일}}`

- 내보낸 모든 함수 나열:

`readpe --exports {{경로/대상/실행파일}}`
