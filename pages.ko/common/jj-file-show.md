# jj file show

> `jj` 저장소의 특정 리비전에 있는 파일 내용을 출력.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-show>.

- 작업 복사본에 있는 파일 내용 출력:

`jj file show {{경로/대상/파일}}`

- 지정한 리비전에 있는 파일 내용 출력:

`jj file show {{[-r|--revision]}} {{revision}} {{경로/대상/파일}}`

- 디렉터리 아래 모든 파일 내용을 재귀적으로 출력:

`jj file show {{경로/대상/디렉터리}}`

- 사용자 지정 템플릿을 사용해 파일 메타데이터 출력:

`jj file show {{[-T|--template]}} "{{템플릿}}" {{경로/대상/파일}}`
