# gup

> `go install`로 설치된 바이너리를 병렬로 업데이트하는 도구.
> 더 많은 정보: <https://github.com/nao1215/gup#how-to-use>.

- 설치된 모든 바이너리 업데이트:

`gup update`

- 설치된 모든 바이너리, 패키지 경로 및 버전 목록 표시:

`gup list`

- 실제 설치 없이 사용 가능한 업데이트 확인:

`gup check`

- 설치된 바이너리 목록을 파일로 내보내기:

`gup export {{[-f|--file]}} {{경로/대상/gup.json}}`

- `gup` 설정 파일로부터 바이너리 설치:

`gup import {{[-f|--file]}} {{경로/대상/gup.json}}`

- 특정 바이너리 제거:

`gup remove {{바이너리_이름}}`

- 특정 바이너리를 제외하고 모든 바이너리 업데이트:

`gup update {{[-e|--exclude]}} {{바이너리1,바이너리2,...}}`

- 특정 바이너리를 최신 버전으로 업데이트:

`gup update --latest {{바이너리1,바이너리2,...}}`
