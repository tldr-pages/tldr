# jj file annotate

> `jj` 저장소 내 대상 파일에서 각 줄이 어떠한 변경에서 유래했는지 표시.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-annotate>.

- 작업 복사본의 파일을 줄 단위로 분석하여 변경 출처 표시:

`jj file annotate {{경로/대상/파일}}`

- 지정한 리비전을 기준으로 파일 각 줄에 대한 변경 출처 표시:

`jj file annotate {{[-r|--revision]}} {{리비전}} {{경로/대상/파일}}`

- 사용자 지정 템플릿을 사용하여 파일 각 줄에 대한 변경 출처 표시:

`jj file annotate {{[-T|--template]}} "{{템플릿}}" {{경로/대상/파일}}`
